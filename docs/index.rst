Welcome to pycli_tools's documentation!
=======================================

A python module to help create predictable command line tools

`pycli_tools` is a python module that wraps the :py:class:`ArgumentParser`
class from the build-in :py:mod:`argparse` module. 

If you use it in your command line scripts you will get some defaults options
added to your application such as `--verbose` and `--quiet` to control the
verbosity of your application (using the python :py:mod:`logging` module). 

Also there is the `--config` option that gives you the ability to read command
line arguments from a configuration file to save users of your application a
lot of typing (e.g. `~/.myapprc`).

Contents:

.. toctree::
   :maxdepth: 2

   installation
   usage
   examples
   documentation


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
