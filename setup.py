from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="almanac_extractors",
    version="0.1.0",
    author="piyush tyagi",
    author_email="piyushtyagi28@hotmail.com",
    description="Extractor of files from different providers like github, gitlab, quip etc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/piyush1856/almanac-extractors",
    project_urls={
        "Documentation": "https://github.com/piyush1856/almanac-extractors/blob/main/README.md",
        "Source Code": "https://github.com/piyush1856/almanac-extractors",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.10",
    install_requires=[
        "httpx>=0.28.1",
        "beautifulsoup4>=4.12.0",
        "pydantic>=2.11.3",
        "asyncio>=3.4.3",
        "uuid>=1.30",
        "structlog>=23.1.0",
        "structlog-sentry>=2.0.0",
        "pytz>=2023.3"
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.1",
            "black>=23.3.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.3.0"
        ]
    },
)