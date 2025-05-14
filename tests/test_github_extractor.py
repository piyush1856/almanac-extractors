import pytest
from unittest.mock import patch, AsyncMock, MagicMock

from extractors.extractor import GitHubRepoExtractor
from tests.test_inputs import GITHUB_INPUTS


@pytest.fixture
def github_extractor():
    """Create a GitHub extractors instance with valid credentials."""
    inputs = GITHUB_INPUTS["valid"]
    return GitHubRepoExtractor(
        repo_url=inputs["repo_url"],
        pat=inputs["pat"],
        branch_name=inputs["branch_name"]
    )


class TestGitHubRepoExtractor:
    
    def test_validate_url(self):
        """Test URL validation logic."""
        # Valid URL
        valid_extractor = GitHubRepoExtractor(
            repo_url=GITHUB_INPUTS["valid"]["repo_url"],
            pat="token",
            branch_name="main"
        )
        valid_extractor._validate_url()  # Should not raise exception
        
        # Invalid URL - Use pytest.raises as a context manager
        with pytest.raises(ValueError):
            GitHubRepoExtractor(
                repo_url=GITHUB_INPUTS["invalid_url"]["repo_url"],
                pat="token",
                branch_name="main"
            )
    
    def test_get_clone_url(self, github_extractor):
        """Test generation of clone URL."""
        clone_url = github_extractor._get_clone_url()
        assert "https://" in clone_url
        assert github_extractor.pat in clone_url
        assert "github.com" in clone_url
    
    @pytest.mark.asyncio
    async def test_is_project_public(self, github_extractor):
        """Test checking if a GitHub repository is public."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await github_extractor.is_project_public()
            assert result is True
            
            # Test private repo
            mock_response.status_code = 404
            result = await github_extractor.is_project_public()
            assert result is False
    
    @pytest.mark.asyncio
    async def test_validate_credentials_success(self, github_extractor):
        """Test successful credential validation."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_instance = AsyncMock()
            mock_client.return_value.__aenter__.return_value = mock_instance
            
            # Mock successful responses
            repo_response = AsyncMock()
            repo_response.status_code = 200
            repo_response.json.return_value = {"name": "repo"}
            
            branch_response = AsyncMock()
            branch_response.status_code = 200
            
            mock_instance.get.side_effect = [repo_response, branch_response]
            
            result = await github_extractor.validate_credentials()
            
            assert result["is_valid"] is True
            assert result["url_valid"] is True
            assert result["token_valid"] is True
            assert result["branch_valid"] is True
    
    @pytest.mark.asyncio
    async def test_validate_credentials_invalid_token(self, github_extractor):
        """Test validation with invalid token."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_instance = AsyncMock()
            mock_client.return_value.__aenter__.return_value = mock_instance
            
            # Mock unauthorized response
            repo_response = AsyncMock()
            repo_response.status_code = 401
            
            mock_instance.get.return_value = repo_response
            
            result = await github_extractor.validate_credentials()
            
            assert result["is_valid"] is False
            assert result["token_valid"] is False
            assert "Invalid access token" in result["message"]