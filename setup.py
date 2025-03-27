from setuptools import setup, find_packages

setup(
    name="random_sort",
    version="0.1.0",
    packages=find_packages(),
    description="A library that sorts lists randomly",
    long_description="Random Sort is a joke library that implements a sorting algorithm based on randomness. It repeatedly shuffles a list until it happens to be sorted.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/random_sort",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 