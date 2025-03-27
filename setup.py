from setuptools import setup, find_packages
import os

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="random_sort",
    version="0.1.1",
    packages=find_packages(),
    description="A Python library that implements a sort algorithm based on randomization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/FrancescoGrazioso/random_sort",
    project_urls={
        "Bug Tracker": "https://github.com/FrancescoGrazioso/random_sort/issues",
        "Documentation": "https://github.com/FrancescoGrazioso/random_sort",
        "Source Code": "https://github.com/FrancescoGrazioso/random_sort",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="sort, random, bogosort, algorithm, humor",
    python_requires=">=3.6",
) 