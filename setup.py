# Setup script to install the package

# setup.py

from setuptools import find_packages, setup

setup(
    name="utilz",
    version="0.0.1",
    packages=find_packages(),
    description="A collection of utility functions for various tasks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Souvik Das",
    author_email="souvikdas.dev@gmail.com",
    url="https://github.com/souvikdas-dev/utilz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
