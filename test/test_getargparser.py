import os
import sys
from nose.tools import raises

from pycli_tools import get_argparser



sys.argv = ['pycli_test']


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
    arguments = '-c test/tests.conf'.split()
    parser = get_argparser(prog='myapp', version='1.7',
                           default_config='~/.myapprc',
                           arguments=arguments)
    args = parser.parse_args()
    assert args.config_file == 'test/tests.conf'
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


@raises(SystemExit)
def test_with_nonexistent_configfile():
    arguments = '-vvv -c test.config'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()


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


if '__main__' == __name__:
    parser = get_argparser(default_config='~/.pycli_toolsrc')
    args = parser.parse_args()
    print args
