# -*- coding: utf-8 -*-
import re
import codecs

from setuptools import setup
from setuptools.command.test import test as TestCommand


class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])


setup(
    name = 'pycli_tools',
    description = 'A python module to help create predictable command line tools for python >= 2.6 and 3.x',
    version = re.search(r'''^__version__\s*=\s*["'](.*)["']''', open('pycli_tools/__init__.py').read(), re.M).group(1),
    author = 'Nico Di Rocco',
    author_email = 'dirocco.nico@gmail.com',
    url = 'http://nrocco.github.io/',
    license = 'GPLv3',
    download_url = 'http://github.com/nrocco/pycli-tools',
    long_description = codecs.open('README.rst', 'rb', 'utf-8').read(),
    include_package_data = True,
    zip_safe = False,
    tests_require = [
        'nose',
        'mock',
        'coverage',
    ],
    packages = [
        'pycli_tools'
    ],
    classifiers = [
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    cmdclass = {
        'test': NoseTestCommand
    }
)
