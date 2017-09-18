#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup(
    name="utcdtw-cffi",
    version="0.1",
    description="CFFI binding for UTC DTW suite",
    long_description=open("README.rst", "rt").read(),
    url="utcdtw-cffi.local",
    author="Dimitri Vorona",
    author_email="vorona@in.tum.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(),
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=[
        "./ucrdtw_cffi/cffi.py:ffi",
    ],
)
