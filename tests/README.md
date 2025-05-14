# Tests for Almanac Extractors

This directory contains tests for the Almanac Extractors library.

## Test Structure

- `conftest.py`: Contains pytest fixtures used across multiple test files
- `test_inputs.py`: Contains test input data for all extractors
- `test_github_extractor.py`: Tests for GitHub repository extraction
- `test_azure_extractor.py`: Tests for Azure DevOps repository extraction
- `test_quip_extractor.py`: Tests for Quip document extraction

## Running Tests

To run all tests:

```bash
pytest
```

To run tests for a specific extractor:

```bash
pytest tests/test_github_extractor.py
pytest tests/test_azure_extractor.py
pytest tests/test_quip_extractor.py
```

To run tests with verbose output:

```bash
pytest -v
```

## Environment Variables

The tests use mocked environment variables by default (see `conftest.py`). If you want to run tests against real services, you can set the following environment variables:

```bash
export GITHUB_TOKEN="your_github_token"
export AZURE_PAT="your_azure_pat"
export QUIP_TOKEN="your_quip_token"
```

## Adding New Tests

When adding new tests:

1. Add test input data to `test_inputs.py`
2. Create test fixtures in `conftest.py` if needed across multiple test files
3. Follow the existing pattern of using pytest fixtures and mocking external services

## Test Coverage

To run tests with coverage report:

```bash
pytest --cov=extractors
```

To generate an HTML coverage report:

```bash
pytest --cov=extractors --cov-report=html
```

The HTML report will be available in the `htmlcov` directory.
