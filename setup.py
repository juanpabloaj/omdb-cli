# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="omdb-cli",
    version="0.1.0",
    description="A command line tool for The Open Movie Database API",
    license="MIT",
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    url="https://github.com/juanpabloaj/omdb-cli",
    packages=find_packages(),
    install_requires=['omdb'],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'omdb=omdbcli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ]
)
