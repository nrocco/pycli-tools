pycli_tools
===========

  A python module to help create predictable command line tools for python >= 2.6 and 3.x

`pycli_tools` is a python module that wraps the :py:class:`ArgumentParser`
class from the build-in :py:mod:`argparse` module. 

If you use it in your command line scripts you will get some defaults options
added to your application such as `--verbose` and `--quiet` to control the
verbosity of your application (using the python :py:mod:`logging` module). 

Also there is the `--config` option that gives you the ability to read command
line arguments from a configuration file to save users of your application a
lot of typing (e.g. `~/.myapprc`).


| Copyright (c) 2013 Nico Di Rocco.
| License: MIT (see `LICENSE <https://github.com/nrocco/pycli-tools/blob/master/LICENSE>`_ for details).



installation
------------

The easiest way is to install using pip:

.. code-block:: bash

   $ pip install pycli_tools


Read the documentation for `alternative ways of installing <http://pythonhosted.org/pycli_tools/installation.html>`_.



usage
-----

To create a `myapp` command that reads its default configuration from
`~/.myapprc` do this:

.. code-block:: python

   from pycli_tools.parsers import get_argparser

   parser = get_argparser(prog='myapp', default_config='~/.myapprc')
   parser.add_argument('--database')
   parser.add_argument('file')
   args = parser.parse_args()


The file `~/.myapprc` can contain the following:

.. code-block:: python

   [myapp]
   database = /some/path/to/my/database.sqlite


Read the documentation to see `how to use pycli_tools <http://pythonhosted.org/pycli_tools/usage.html>`_.



documentation
-------------

Read `the full documentation <http://pythonhosted.org/pycli_tools/>`_ here.
