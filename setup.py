from setuptools import setup, find_packages

setup(
    name="graex-algoscope",
    version="0.1.0",
    description="EDR for SEO: Algorithmic SEO Intelligence Platform",
    author="Grae-X Labs",
    author_email="dev@graexlabs.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "pydantic>=2.5.0",
        "click>=8.1.7",
        "rich>=13.7.0",
        "aiohttp>=3.9.1",
        "lxml>=4.9.3",
        "python-dateutil>=2.8.2",
        "tqdm>=4.66.1",
        "html5lib>=1.1",
    ],
    entry_points={
        "console_scripts": [
            "graex=src.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
)
