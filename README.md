# Almanac Extractors

A Python library for extracting files from different providers like GitHub, GitLab, Azure DevOps, and Quip.

## Features

- Extract files from Git repositories (GitHub, GitLab, Azure DevOps)
- Extract documents from Quip
- Asynchronous operation for improved performance
- Comprehensive metadata for extracted content
- Authentication support for private repositories

## Installation

```bash
pip install almanac-extractors
```

Or install from source:

```bash
git clone https://github.com/piyush1856/almanac-extractors.git
cd almanac-extractors
pip install -e .
```

## Usage

### GitHub Repository Extraction

```python
import asyncio
from almanac_extractors.extractor import GitHubRepoExtractor

async def main():
    # Initialize with repository URL, branch name, and personal access token (optional for public repos)
    extractor = GitHubRepoExtractor(
        repo_url="https://github.com/username/repo",
        branch_name="main",
        pat="your_github_token"  # Optional for public repositories
    )
    
    # Validate credentials
    validation = await extractor.validate_credentials()
    if validation["is_valid"]:
        # Extract repository contents
        files = await extractor.extract()
        print(f"Extracted {len(files)} files")
    else:
        print(f"Validation failed: {validation['message']}")

if __name__ == "__main__":
    asyncio.run(main())
```

### GitLab Repository Extraction

```python
import asyncio
from almanac_extractors.extractor import GitLabRepoExtractor

async def main():
    extractor = GitLabRepoExtractor(
        repo_url="https://gitlab.com/username/repo",
        branch_name="main",
        pat="your_gitlab_token"
    )
    
    # Extract repository contents
    files = await extractor.extract()
    print(f"Extracted {len(files)} files")

if __name__ == "__main__":
    asyncio.run(main())
```

### Azure DevOps Repository Extraction

```python
import asyncio
from almanac_extractors.extractor import AzureDevopsRepoExtractor

async def main():
    extractor = AzureDevopsRepoExtractor(
        repo_url="https://username@dev.azure.com/organization/project/_git/repo",
        branch_name="main",
        pat="your_azure_pat"
    )
    
    # Extract repository contents
    files = await extractor.extract()
    print(f"Extracted {len(files)} files")

if __name__ == "__main__":
    asyncio.run(main())
```

### Quip Document Extraction

```python
import asyncio
from almanac_extractors.extractor import QuipExtractor

async def main():
    # Initialize with access token and list of Quip document/folder URLs
    extractor = QuipExtractor(
        pat="your_quip_token",
        urls=["https://quip.com/document_id", "https://quip.com/folder_id"]
    )
    
    # Extract documents
    documents = await extractor.extract()
    print(f"Extracted {len(documents)} documents")

if __name__ == "__main__":
    asyncio.run(main())
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/piyush1856/almanac-extractors.git
cd almanac-extractors

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
