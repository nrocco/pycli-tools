#!/usr/bin/env python
from setuptools import setup
import pycli_tools

setup(
    name = 'pycli_tools',
    version = pycli_tools.__version__,
    packages = [
        'pycli_tools'
    ],
    download_url = 'http://github.com/nrocco/pycli-tools',
    url = 'http://nrocco.github.io/',
    author = pycli_tools.__author__,
    author_email = 'dirocco.nico@gmail.com',
    description = 'A python module to help create predictable command line tools for python >= 2.6 and 3.x',
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
