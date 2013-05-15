#!/usr/bin/env python
import os, sys; sys.path.insert(0, os.path.abspath('..'))

from pycli_tools.parsers import get_argparser

parser = get_argparser(prog='myapp', default_config='~/.myapprc')
parser.add_argument('--database')
parser.add_argument('file')
args = parser.parse_args()
