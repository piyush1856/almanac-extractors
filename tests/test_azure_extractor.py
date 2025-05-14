import pytest
from unittest.mock import patch, AsyncMock

from extractors.extractor import AzureDevopsRepoExtractor
from tests.test_inputs import AZURE_INPUTS


@pytest.fixture
def azure_extractor():
    """Create an Azure DevOps extractors instance with valid credentials."""
    inputs = AZURE_INPUTS["valid"]
    return AzureDevopsRepoExtractor(
        repo_url=inputs["repo_url"],
        pat=inputs["pat"],
        branch_name=inputs["branch_name"]
    )


class TestAzureDevopsRepoExtractor:
    
    def test_validate_url(self):
        """Test URL validation logic."""
        # Valid URL
        valid_extractor = AzureDevopsRepoExtractor(
            repo_url=AZURE_INPUTS["valid"]["repo_url"],
            pat="token",
            branch_name="main"
        )
        valid_extractor._validate_url()  # Should not raise exception
        
        # Invalid URL - Use pytest.raises as a context manager
        with pytest.raises(ValueError):
            AzureDevopsRepoExtractor(
                repo_url=AZURE_INPUTS["invalid_url"]["repo_url"],
                pat="token",
                branch_name="main"
            )
    
    def test_get_clone_url(self, azure_extractor):
        """Test generation of clone URL."""
        clone_url = azure_extractor._get_clone_url()
        assert "https://" in clone_url
        assert azure_extractor.pat in clone_url
        assert "dev.azure.com" in clone_url
    
    @pytest.mark.asyncio
    async def test_is_project_public(self, azure_extractor):
        """Test checking if an Azure DevOps project is public."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_response = AsyncMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"visibility": "public"}
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await azure_extractor.is_project_public()
            assert result is True
            
            # Test private project
            mock_response.json.return_value = {"visibility": "private"}
            result = await azure_extractor.is_project_public()
            assert result is False
    
    @pytest.mark.asyncio
    async def test_validate_credentials_success(self, azure_extractor):
        """Test successful credential validation."""
        with patch("httpx.AsyncClient") as mock_client:
            mock_instance = AsyncMock()
            mock_client.return_value.__aenter__.return_value = mock_instance
            
            # Mock successful responses
            repo_response = AsyncMock()
            repo_response.status_code = 200
            
            branch_response = AsyncMock()
            branch_response.status_code = 200
            branch_response.json.return_value = {"value": ["main"]}
            
            mock_instance.get.side_effect = [repo_response, branch_response]
            
            result = await azure_extractor.validate_credentials()
            
            assert result["is_valid"] is True
            assert result["url_valid"] is True
            assert result["token_valid"] is True
            assert result["branch_valid"] is True