Gitone
======

Combine multiple **git** version controls steps into **one** command.

|PyPI| |Updates|

Introduction
------------

Unlike git shell commands, ``gitone`` automatically generates commit messages with every command.

The ``gitone`` Python package consists of 8 shell commands and
functions:

- ``camp``, which stands for ``git commit -am`` and ``git push``, will add and commit all changes made to tracked files and push the commit to the remote repository.
- ``acmp``, which stands for ``git add``, ``git commit -m`` and ``git push``, will add and commit all changes made to all files and push the changes to the remote repository.
- ``cam``, which stands for ``git commit -am``, will add and commit all changes made to tracked files.
- ``acm``, which stands for ``git add``, ``git commit -m`` and ``git push``, will add and commit all changes made to all files.

and the ``--amend`` version of the above function:

- ``camendamp``, which stands for ``git commit --amend -am`` and ``git push --force``, will overwrite the previous commit by adding and committing all changes made to tracked files and then force push the overwritten commit to the remote repository.
- ``acamendmp``, which stands for ``git add``, ``git commit --amend -m`` and ``git push --force``, will overwrite the previous commit by adding and committing all changes made to all files and then force push the overwritten commit to the remote repository.
- ``camendam``, which stands for ``git commit --amend -am``, will overwrite the previous commit by adding and committing all changes made to tracked files.
- ``acamendm``, which stands for ``git add``, ``git commit --amend -m``, will overwrite the previous commit by adding and committing all changes made to all files.


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
