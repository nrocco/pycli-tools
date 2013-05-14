Installation
============

There are various ways of installing `pycli_tools`


Install using pip
-----------------

Install the latest stable version using pip.

.. code-block:: bash

   $ pip install pycli_tools


Install bleeding-edge from github using pip
-------------------------------------------

The plus side is you get the latest version from github. The downside of this
method is that future upgrades are harder unless you remember the github url

.. code-block:: bash

   $ pip install -e git+https://github.com/nrocco/pycli-tools#egg=pycli_tools-dev


Install bleeding-edge from github manually
------------------------------------------

Clone this git repository to get the latest version and install using
setuptools or distribute.

.. code-block:: bash

   $ git clone https://github.com/nrocco/pycli-tools
   $ cd pycli-tools
   $ python setup.py install


Install for the purpose of developing/contributing
--------------------------------------------------

Additional pip packages are required such as :py:mod:`nose` for running unit
tests, :py:mod:`coverage` for generating code coverage reports and
:py:mod:`sphinx` for generating documentation.

.. code-block:: bash

   $ git clone https://github.com/nrocco/pycli-tools
   $ cd pycli-tools
   $ python setup.py develop

