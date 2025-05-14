"""
Test input values for extractors tests.
This file contains all the test data used by the test suite.
"""

# GitHub repository test inputs
GITHUB_INPUTS = {
    "valid": {
        "repo_url": "https://github.com/username/repo",
        "pat": "ghp_validpersonalaccesstoken",
        "branch_name": "main"
    },
    "invalid_url": {
        "repo_url": "https://invalid-github.com/username/repo",
        "pat": "ghp_validpersonalaccesstoken",
        "branch_name": "main"
    },
    "invalid_token": {
        "repo_url": "https://github.com/username/repo",
        "pat": "invalid_token",
        "branch_name": "main"
    },
    "invalid_branch": {
        "repo_url": "https://github.com/username/repo",
        "pat": "ghp_validpersonalaccesstoken",
        "branch_name": "nonexistent_branch"
    }
}

# Azure DevOps repository test inputs
AZURE_INPUTS = {
    "valid": {
        "repo_url": "https://username@dev.azure.com/organization/project/_git/repo",
        "pat": "validpersonalaccesstoken",
        "branch_name": "main"
    },
    "invalid_url": {
        "repo_url": "https://invalid-azure.com/organization/project/_git/repo",
        "pat": "validpersonalaccesstoken",
        "branch_name": "main"
    },
    "invalid_token": {
        "repo_url": "https://username@dev.azure.com/organization/project/_git/repo",
        "pat": "invalid_token",
        "branch_name": "main"
    },
    "invalid_branch": {
        "repo_url": "https://username@dev.azure.com/organization/project/_git/repo",
        "pat": "validpersonalaccesstoken",
        "branch_name": "nonexistent_branch"
    }
}

# Quip test inputs
QUIP_INPUTS = {
    "valid": {
        "pat": "validquiptoken",
        "urls": ["https://quip.com/validDocumentId", "https://quip.com/validFolderId"],
        "max_docs_per_kb": 10
    },
    "invalid_token": {
        "pat": "invalidquiptoken",
        "urls": ["https://quip.com/validDocumentId"],
        "max_docs_per_kb": 10
    },
    "invalid_urls": {
        "pat": "validquiptoken",
        "urls": ["https://quip.com/invalidId", "https://invalid-quip.com/someId"],
        "max_docs_per_kb": 10
    }
}