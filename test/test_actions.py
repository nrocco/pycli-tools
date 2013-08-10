import os
import sys
from nose.tools import raises

# Make sure that pycli_tools module is in the path
test_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(test_root))

from pycli_tools.parsers import get_argparser
from pycli_tools.actions import ExistingFileAction


@raises(SystemExit)
def test_action_file_not_exists():
    arguments = '--database non-existent.txt'.split()
    parser = get_argparser(prog='myapp', version='1.7',
                           arguments=arguments)
    parser.add_argument('--database', action=ExistingFileAction)
    args = parser.parse_args()

def test_action_file_exists():
    arguments = '--database %s' % os.path.abspath(__file__)
    parser = get_argparser(prog='myapp', version='1.7',
                           arguments=arguments.split())
    parser.add_argument('--database', action=ExistingFileAction)
    args = parser.parse_args()
