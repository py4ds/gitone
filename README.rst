Gitone: Combine multiple **git** version controls steps into **one**
====================================================================

|Build| |Chat| |License| |PyPI| |Status| |Updates| |Versions|

Introduction
------------

The ``gitone`` Python package takes some of the tedium out of `git <https://git-scm.com/>`__ version control by rolling multiple git shell commands into one shell command or Python function.

Unlike git shell commands, ``gitone`` shell commands and Python functions can automatically generate commit messages if a commit message is not provided!

You can use ``gitone`` in

- your terminal (e.g. ``bash``, ``zsh``, ``fish``, etc.) or
- your favorite Python environment (e.g. `PyCharm <https://www.jetbrains.com/pycharm/>`__ or `Visual Studio Code <https://code.visualstudio.com/docs/python/python-tutorial>`__).


The ``gitone`` Python package consists of 8 shell commands and Python functions:

- ``cam``, which stands for ``git commit -am``, will add and commit all changes made to tracked files.
- ``camp``, which stands for ``git commit -am && git push``, will add and commit all changes made to tracked files and push the commit to the remote repository.
- ``acm``, which stands for ``git add --all && git commit -m``, will add and commit all changes made to all files and push the changes to the remote repository.
- ``acmp``, which stands for ``git add --all && git commit -m && git push``, will add and commit all changes made to all files and push the changes to the remote repository.

In summary, ``cam`` and ``camp`` work on only tracked files (those that have previously been added to git's index),
while ``acm`` and ``acmp`` work on all files by adding untracked files to git's index.

There are also the ``--amend`` versions of the above:

- ``amend``, which is short for ``git commit --amend -am``, will overwrite the previous commit by adding and committing all changes made to tracked files.
- ``amendp``, which is short for ``git commit --amend -am && git push --force``, will overwrite the previous commit by adding and committing all changes made to tracked files and then force push the overwritten commit to the remote repository.
- ``aamend``, which is short for ``git add --all && git commit --amend -m``, will overwrite the previous commit by adding and committing all changes made to all files.
- ``aamendp``, which is short for ``git add --all && git commit --amend -m && git push --force``, will overwrite the previous commit by adding and committing all changes made to all files and then force push the overwritten commit to the remote repository.

Similarly to the first four, ``amend`` and ``amendp`` work on only tracked files (those that have previously been added to git's index),
while ``aamend`` and ``aamendp`` work on all files by adding untracked files to git's index.

All ``gitone`` functions and commands rely on the `GitPython <https://gitpython.readthedocs.io/>`__ Python library.
The command line interface relies on the `click <https://click.palletsprojects.com/>`__ Python library.

Documentation and Code
----------------------

The documentation is hosted at https://py4ds.github.io/gitone/.

The code is hosted at https://github.com/py4ds/gitone.

Installation
------------

.. code-block:: shell

    $ pip install gitone

Usage
-----

Run any of the available shell commands or Python functions without arguments and a commit message will be automatically generated.

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

When using the shell commands. Do not wrap the commit message in quotes (``""``) or they will be included in the commit message.

.. code-block:: shell

    $ camp Made some changes.
    $ acmp Lemme try something.
    $ cam Not sure what changed.
    $ acm Should be OK now.

To overwrite the previous commit, you can use the amend functions.

If you do not provide a commit message, the previous commit message will be reused.

.. code-block:: python

    >>> amend()
    >>> amendp()
    >>> aamend()
    >>> aamendp()

.. code-block:: shell

    $ amend
    $ amendp
    $ aamend
    $ aamendp

Next Steps
----------

Setting up a repo can be a pain.

- Write an ``init`` function and command to handle all of the repo setup steps like in `this Makefile <https://github.com/py4ds/cookiecutter/blob/master/%7B%7Bcookiecutter.repo%7D%7D/Makefile#L21>`__. Inspired by the `usethis <https://usethis.r-lib.org/reference/use_github.html>`__ R package.

.. |Build| image:: https://travis-ci.org/py4ds/gitone.svg?branch=master
    :target: https://travis-ci.org/py4ds/gitone
.. |Chat| image:: https://badges.gitter.im/py4ds/gitone.svg
   :alt: Join the chat at https://gitter.im/py4ds/gitone
   :target: https://gitter.im/py4ds/gitone?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |License| image:: https://img.shields.io/badge/License-MIT-brightgreen.svg
   :target: https://opensource.org/licenses/MIT
.. |PyPI| image:: https://img.shields.io/pypi/v/gitone.svg
   :target: https://pypi.python.org/pypi/gitone
.. |Status| image:: https://www.repostatus.org/badges/latest/active.svg
   :alt: Project Status: Active – The project has reached a stable, usable state and is being actively developed.
   :target: https://www.repostatus.org/#active
.. |Updates| image:: https://pyup.io/repos/github/py4ds/gitone/shield.svg
   :target: https://pyup.io/repos/github/py4ds/gitone/
.. |Versions| image:: https://img.shields.io/pypi/pyversions/gitone.svg
   :alt: PyPI - Python Version
   :target: https://www.python.org/downloads/
