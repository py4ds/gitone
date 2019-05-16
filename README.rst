Gitone
======

Combine multiple **git** version controls steps into **one** command.

|PyPI| |Updates|

Introduction
------------

Unlike git shell commands, ``gitone`` automatically generates commit messages with every command.

The ``gitone`` Python package consists of 8 shell commands and
functions:

- ``cam``, which stands for ``git commit -am``, will add and commit all changes made to tracked files.
- ``camp``, which stands for ``git commit -am && git push``, will add and commit all changes made to tracked files and push the commit to the remote repository.
- ``acm``, which stands for ``git add --all && git commit -m``, will add and commit all changes made to all files and push the changes to the remote repository.
- ``acmp``, which stands for ``git add --all && git commit -m && git push``, will add and commit all changes made to all files and push the changes to the remote repository.

and the ``--aamend`` version of the above function:

- ``aamend``, which is short for ``git commit --aamend -am``, will overwrite the previous commit by adding and committing all changes made to tracked files.
- ``aamendp``, which is short for ``git commit --aamend -am && git push --force``, will overwrite the previous commit by adding and committing all changes made to tracked files and then force push the overwritten commit to the remote repository.
- ``aamend``, which is short for ``git add --all && git commit --aamend -m``, will overwrite the previous commit by adding and committing all changes made to all files.
- ``aamendp``, which is short for ``git add --all && git commit --aamend -m && git push --force``, will overwrite the previous commit by adding and committing all changes made to all files and then force push the overwritten commit to the remote repository.


Installation
------------

.. code-block:: shell

    $ pip install gitone

Usage
-----


Just run one of available shell commands or Python functions without arguments and a commit message will be automatically generated.

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

You can also pass a commit message to any of the functions or shell commands.

.. code-block:: python

    >>> camp(message="Made some changes.")
    >>> acmp("Lemme try something.")
    >>> cam("Not sure what changed.")
    >>> acm("Should be OK now.")

.. code-block:: shell

    $ camp Made some changes.
    $ acmp Lemme try something.
    $ cam Not sure what changed.
    $ acm Should be OK now.

To overwrite the previous commit, you can use the aamend functions.

If you do not provide a commit message, the previous commit message will be reused.

.. code-block:: python

    >>> aamend()
    >>> aamendp()
    >>> aamend()
    >>> aamendp()

.. code-block:: shell

    $ aamend
    $ aamendp
    $ aamend
    $ aamendp

.. |PyPI| image:: https://img.shields.io/pypi/v/gitone.svg
   :target: https://pypi.python.org/pypi/gitone
.. |Updates| image:: https://pyup.io/repos/github/marskar/gitone/shield.svg
   :target: https://pyup.io/repos/github/marskar/gitone/
