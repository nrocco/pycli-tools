#!/usr/bin/env python
import os, sys; sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))

from pycli_tools.parsers import get_argparser

parser = get_argparser(prog='myapp', version='0.1',
                       default_config=['/etc/myapp.ini', '~/.myapprc'])
parser.add_argument('--database')
parser.add_argument('file')
args = parser.parse_args()

for key, value in args.__dict__.iteritems():
    print '{:<24} = {}'.format(key, value)
