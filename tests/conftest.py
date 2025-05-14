import pytest
import asyncio
import os
from unittest.mock import patch

# Define pytest fixtures that can be used across all test files

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {
        "GITHUB_TOKEN": "mock_github_token",
        "AZURE_PAT": "mock_azure_pat",
        "QUIP_TOKEN": "mock_quip_token"
    }):
        yield

@pytest.fixture
def mock_httpx_client():
    """Mock httpx client for testing HTTP requests."""
    with patch("httpx.AsyncClient") as mock_client:
        yield mock_client