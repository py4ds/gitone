Gitone
======

Combine multiple **git** version controls steps into **one** command.

|PyPI| |Updates|

Introduction
------------

Unlike git shell commands, ``gitone`` automatically generates commit messages with every command.

The ``gitone`` Python package consists of 4 shell commands and
functions:

- ``camp``, which stands for ``git commit -am`` and ``git push`` will add and commit all changes made to tracked files and push the commit to the remote repository.
- ``acmp``, which stands for ``git add``, ``git commit -m`` and ``git push`` will add and commit all changes made to all files and push the changes to the remote repository.
- ``cam``, which stands for ``git commit -am`` and ``git push`` will add and commit all changes made to tracked files.
- ``acm``, which stands for ``git add``, ``git commit -m`` and ``git push`` will add and commit all changes made to all files.


Installation
------------

.. code-block:: shell

    $ pip install gitone

Usage
-----

No need to pass any arguments.

Just run one of available shell commands or Python functions.

.. code-block:: python

    >>> camp()
    >>> acmp()
    >>> cam()
    >>> acm()

.. code-block:: shell

    $ camp
    $ acmp
    $ cam
    $ acm


.. |PyPI| image:: https://img.shields.io/pypi/v/gitone.svg
   :target: https://pypi.python.org/pypi/gitone
.. |Updates| image:: https://pyup.io/repos/github/marskar/gitone/shield.svg
   :target: https://pyup.io/repos/github/marskar/gitone/
