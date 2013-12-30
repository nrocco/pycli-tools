#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'pycli_tools',
                       '__init__.py'), 'rb') as file:
    content = file.read()
    VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(content).group(1)
    AUTHOR = re.compile(r".*__author__ = '(.*?)'", re.S).match(content).group(1)


setup(
    name = 'pycli_tools',
    description = 'A python module to help create predictable command line tools for python >= 2.6 and 3.x',
    version = VERSION,

    packages = find_packages(),
    download_url = 'http://github.com/nrocco/pycli-tools',
    url = 'http://nrocco.github.io/',

    author = AUTHOR,
    author_email = 'dirocco.nico@gmail.com',

    long_description = open('README.rst').read(),
    include_package_data = True,
    license = open('LICENSE').read(),
    zip_safe = False,
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
