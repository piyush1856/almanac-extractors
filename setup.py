from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements-dev.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='almanac_extractors',
    version='0.1.0',
    author='Piyush Tyagi',
    author_email='piyushtyagi28@hotmail.com',
    description='A Python library for extracting files from different providers like GitHub, GitLab, Azure DevOps, and Quip.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/piyush1856/almanac_extractors',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            # 'command-name=package.module:function',
        ],
    },
)