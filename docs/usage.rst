Usage
=====

Use the :py:func:`get_argparser` helper function instead of creating your own
:py:class:`ArgumentParser` instance like you're used to. 

Save the following snippet as a file `myapp.py`.

.. code-block:: python

    from pycli_tools import get_argparser
    parser = get_argparser(prog='myapp', version='1.0',
                           default_config='~/.myapprc')
    parser.add_argument('--database')
    parser.add_argument('action')
    args = parser.parse_args()


Try it out for yourself. You will get some default command line options
without doing anything

.. code-block:: bash

   $ python myapp.py -h
   usage: myapp [-h] [-c CONFIG_FILE] [-v] [-q] [-V] [--database DATABASE]

   My Application

   optional arguments:
     -h, --help            show this help message and exit
     -c CONFIG_FILE, --config CONFIG_FILE
                           path to the config file
     -v, --verbose         output more verbose
     -q, --quiet           surpress all output
     -V, --version         show program's version number and exit
     --database DATABASE

   myapp reads its default configuration from ~/.myapprc


The `-c` or `--config` option by default uses the configuration file that you
passed to the `get_argparser` helper function. Defaults are read from that
file from the section with the same name as the `prog` variable. In the above
case `myapp`.

Create the a file `~/.myapprc` with the following content:

.. code-block:: python

    [myapp]
    database = /path/to/my/database.sqlite


Now you don't have to pass `--database` as a command line option.
