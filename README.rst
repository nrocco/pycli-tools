pycli_tools
===========

A python module to help create predictable command line tools


installation
------------

The easiest way is to install using pip:

.. code-block:: bash

   $ pip install pycli_tools

Read the documentation for alternative ways of http://pythonhosted.org/pycli_tools/installation.html


usage
-----

To create `myapp` command that reads its default configuration from
`~/.myapprc` do this:

.. code-block:: python

   from pycli_tools import get_argparser

   parser = get_argparser(prog='myapp', default_config='~/.myapprc')
   parser.add_argument('--database')
   parser.add_argument('file')
   args = parser.parse_args()

The file `~/.myapprc` can contain:

.. code-block:: python

   [myapp]
   database = /some/path/to/my/database.sqlite

Read the documentation for an extensive usage http://pythonhosted.org/pycli_tools/usage.html


documentation
-------------

Read the full documentation here http://pythonhosted.org/pycli_tools/


Copyright (c) 2013 Nico Di Rocco.
License: MIT (see LICENSE for details).
