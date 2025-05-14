import pytest
from unittest.mock import patch, AsyncMock, MagicMock

from extractors.extractor import QuipExtractor
from tests.test_inputs import QUIP_INPUTS


@pytest.fixture
def quip_extractor():
    """Create a Quip extractors instance with valid credentials."""
    inputs = QUIP_INPUTS["valid"]
    return QuipExtractor(
        pat=inputs["pat"],
        urls=inputs["urls"],
        max_docs_per_kb=inputs["max_docs_per_kb"]
    )


class TestQuipExtractor:
    
    def test_init(self):
        """Test initialization of QuipExtractor."""
        inputs = QUIP_INPUTS["valid"]
        extractor = QuipExtractor(
            pat=inputs["pat"],
            urls=inputs["urls"],
            max_docs_per_kb=inputs["max_docs_per_kb"]
        )
        
        assert extractor.pat == inputs["pat"]
        assert extractor.urls == inputs["urls"]
        assert extractor.max_docs_per_kb == inputs["max_docs_per_kb"]
        assert extractor.headers["Authorization"] == f"Bearer {inputs['pat']}"
    
    def test_extract_id_from_url(self, quip_extractor):
        """Test extraction of Quip ID from URL."""
        # Test document URL
        doc_id = "ABC123"
        doc_url = f"https://quip.com/{doc_id}"
        extracted_id = quip_extractor._extract_id_from_url(doc_url)
        assert extracted_id == doc_id
        
        # Test folder URL
        folder_id = "XYZ789"
        folder_url = f"https://quip.com/{folder_id}/folder-name"
        extracted_id = quip_extractor._extract_id_from_url(folder_url)
        assert extracted_id == folder_id
        
        # Test invalid URL
        invalid_url = "https://invalid-url.com"
        extracted_id = quip_extractor._extract_id_from_url(invalid_url)
        assert extracted_id == ""
    
    @pytest.mark.asyncio
    async def test_get_item_type(self, quip_extractor):
        """Test determination of item type (folder or thread)."""
        with patch.object(quip_extractor, "client") as mock_client:
            # Test thread
            folder_resp = AsyncMock()
            folder_resp.status_code = 404
            
            thread_resp = AsyncMock()
            thread_resp.status_code = 200
            
            mock_client.get.side_effect = [folder_resp, thread_resp]
            
            item_type = await quip_extractor._get_item_type("thread_id")
            assert item_type == "thread"
            
            # Test folder
            folder_resp.status_code = 200
            thread_resp.status_code = 404
            
            mock_client.get.side_effect = [folder_resp, thread_resp]
            
            item_type = await quip_extractor._get_item_type("folder_id")
            assert item_type == "folder"
    
    @pytest.mark.asyncio
    async def test_get_folder_name(self, quip_extractor):
        """Test getting folder name with caching."""
        with patch.object(quip_extractor, "client") as mock_client:
            folder_id = "folder123"
            folder_name = "Test Folder"
            
            response = AsyncMock()
            response.status_code = 200
            response.json.return_value = {"title": folder_name}
            
            mock_client.get.return_value = response
            
            # First call should make an API request
            result = await quip_extractor._get_folder_name(folder_id)
            assert result == folder_name
            assert folder_id in quip_extractor.folder_name_cache
            
            # Second call should use the cache
            mock_client.get.reset_mock()
            result = await quip_extractor._get_folder_name(folder_id)
            assert result == folder_name
            mock_client.get.assert_not_called()