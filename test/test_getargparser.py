import os
import sys
from nose.tools import raises

# Make sure that pycli_tools module is in the path
test_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(test_root))

from pycli_tools.parsers import get_argparser


_old_argv = sys.argv
sys.argv = ['pycli_test']


def test_prog_and_version():
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    args = parser.parse_args()
    assert args.prog == 'myapp'
    assert args.version == '1.0'


def test_processing_remaining_argv():
    sys.argv.append('test')
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    parser.add_argument('event')
    args = parser.parse_args()
    assert args.event == 'test'
    sys.argv.pop()


def test_with_default_loglevel():
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    args = parser.parse_args()
    assert args.loglevel == 30
    assert args.quiet == False
    assert args.verbose == 0


def test_with_default_config():
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    args = parser.parse_args()
    assert args.config_file == ['~/.myapprc']
    assert args.default_config_file == ['~/.myapprc']


def test_specify_custom_config():
    arguments = '-c test/myapp.conf'.split()
    parser = get_argparser(prog='myapp', version='1.7',
                           default_config='~/.myapprc',
                           arguments=arguments)
    args = parser.parse_args()
    assert args.config_file == ['test/myapp.conf']
    assert args.default_config_file == ['~/.myapprc']


def test_parsing_config_file():
    parser = get_argparser(prog='myapp', version='1.7',
                           default_config='test/myapp.conf')
    args = parser.parse_args()
    assert args.database == '/some/path/to/my/database.sqlite'


def test_ignoring_config_no_section():
    parser = get_argparser(prog='nonexistentsection', version='1.1.1',
                           default_config='test/myapp.conf')
    args = parser.parse_args()
    assert args.prog == 'nonexistentsection'


def test_parsing_config_file_override():
    sys.argv.append('--database')
    sys.argv.append('mydb.sqlite')
    parser = get_argparser(prog='myapp', version='1.7',
                           default_config='test/myapp.conf')
    parser.add_argument('--database')
    args = parser.parse_args()
    assert args.database == 'mydb.sqlite'
    sys.argv.pop()
    sys.argv.pop()


def test_no_default_config():
    parser = get_argparser(prog='myapp', version='1.0')
    args = parser.parse_args()
    assert args.config_file == []
    assert args.default_config_file == None


def test_without_prog():
    parser = get_argparser()
    args = parser.parse_args()
    assert args.prog == sys.argv[0]


def test_with_nonexistent_configfile():
    arguments = '-vvv -c test.config'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()

    assert True == True


def test_quiet_and_verbose():
    arguments = '-q -vvv'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()
    assert args.loglevel == 100
    assert args.quiet == True
    assert args.verbose == 3


def test_verbose_and_quiet():
    arguments = '-vvv -q'.split()
    parser = get_argparser(arguments=arguments)
    args = parser.parse_args()
    assert args.loglevel == 100
    assert args.quiet == True
    assert args.verbose == 3


def test_argumentparser_desc_and_epilog():
    desc = 'This is a description'
    epilog = 'This is an epilog'

    parser = get_argparser(prog='myapp', default_config='myapp.conf',
                           description=desc, epilog=epilog)
    args = parser.parse_args()

    assert epilog in parser.epilog, 'parser.epilog does not contain the given epilog'
    assert 'myapp reads its default configuration from myapp.conf' in parser.epilog
    assert parser.description == desc, 'Description does not match'
