pycli_tools
===========

A python module to help create predictable command line tools

installation
------------

Install from pip

    $ pip install pycli_tools


usage
-----

Use the `get_argparser` helper function instead of creating your own
ArgumentParser instance like you're used to. Save the following snippet as a
file `myapp.py`

    $ cat myapp.py
    from pycli_tools import get_argparser
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    parser.add_argument('action')
    args = parser.parse_args()


Try it out for yourself. You will get some default command line options
without doing anything

    $ python myapp.py -h
    usage: myapp [-h] [-c CONFIG_FILE] [-v] [-q] [-V] action

    positional arguments:
      action

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_FILE, --config CONFIG_FILE
                            path to the config file
      -v, --verbose         output more verbose
      -q, --quiet           surpress all output
      -V, --version         show program's version number and exit


The `-c` or `--config` option by default uses the configuration file that you
passed to the `get_argparser` helper function. Defaults are read from that
file from the section with the same name as the `prog` variable. In the above
case `myapp`:

    $ cat ~/.myapprc
    [myapp]
    verbose = 10


Now you don't have to pass `-vvv` as a command line option to enable verbose
otuput.
