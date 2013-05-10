#!/usr/bin/env python
from setuptools import setup

setup(
    name = 'pycli_tools',
    version = '1.1',
    packages = [
        'pycli_tools'
    ],
    url = 'http://nrocco.github.io/',
    author = 'Nico Di Rocco',
    author_email = 'dirocco.nico@gmail.com',
    description = 'A python module to help create predictable command line tools',
    include_package_data = True,
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
