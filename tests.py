import os
import sys
from pycli_tools import get_argparser



sys.argv[0] = 'pycli_test'


def test_with_default_config():
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    args = parser.parse_args()
    assert args.config_file == os.path.expanduser('~/.myapprc')
    assert args.default_config_file == '~/.myapprc'
    assert args.loglevel == 30
    assert args.prog == 'myapp'
    assert args.quiet == False
    assert args.verbose == 0
    assert args.version == '1.0'


def test_overriding_default_config():
    arguments = '-c override_me.conf'.split()
    parser = get_argparser(prog='myapp', version='1.7',
                           default_config='~/.myapprc')
    args = parser.parse_args(arguments)
    assert args.config_file == 'override_me.conf'
    assert args.default_config_file == '~/.myapprc'
    assert args.loglevel == 30
    assert args.prog == 'myapp'
    assert args.quiet == False
    assert args.verbose == 0
    assert args.version == '1.7'


def test_no_default_config():
    parser = get_argparser(prog='myapp', version='1.0')
    args = parser.parse_args()
    assert args.config_file == None
    assert args.default_config_file == None
    assert args.loglevel == 30
    assert args.prog == 'myapp'
    assert args.quiet == False
    assert args.verbose == 0
    assert args.version == '1.0'


def test_without_prog():
    parser = get_argparser()
    args = parser.parse_args()
    assert args.config_file == None
    assert args.default_config_file == None
    assert args.loglevel == 30
    assert args.prog == sys.argv[0]
    assert args.quiet == False
    assert args.verbose == 0
    assert args.version == ''


def test_with_arguments():
    arguments = '-vvv -c test.config'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()
    assert args.config_file == 'test.config'
    assert args.default_config_file == None
    assert args.loglevel == 10
    assert args.prog == 'pycli_test'
    assert args.quiet == False
    assert args.verbose == 3
    assert args.version == ''


def test_quiet_and_verbose():
    arguments = '-q -vvv'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()
    assert args.config_file == None
    assert args.default_config_file == None
    assert args.loglevel == 100
    assert args.prog == 'pycli_test'
    assert args.quiet == True
    assert args.verbose == 3
    assert args.version == ''


def test_verbose_and_quiet():
    arguments = '-vvv -q'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()
    assert args.config_file == None
    assert args.default_config_file == None
    assert args.loglevel == 100
    assert args.prog == 'pycli_test'
    assert args.quiet == True
    assert args.verbose == 3
    assert args.version == ''


