#!/usr/bin/env python
from distutils.core import setup
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Notey",
    version="0.1.0",
    packages=find_packages(),
    # metadata to display on PyPI
    author="Vhenrixon",
    author_email="vhenrixon@gmail.com",
    description="Small CLI for creating notes",
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'note = Notey.notes:main'
        ]
    },
    install_requires=[
        'pyfiglet',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
