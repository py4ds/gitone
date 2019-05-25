#!/usr/bin/env python
# -*- coding: utf-8 -*-
import git


def spp() -> None:
    """Stash local changes, pull with ``--rebase``, and pop the latest stash.

    :note: Use ``spp()`` if you try to pull with ``--rebase``
           and get an error that says::

               error: cannot pull with rebase: You have unstaged changes.
               error: please commit or stash them.

           With ``spp()`` the stash is not preserved, so there is not need to
           use ``git stash drop`` to remove the most recent stash.
    """

    repo = git.Repo(search_parent_directories=True)
    print(repo.git.stash('save'),
          repo.git.pull('--rebase'),
          repo.git.stash('pop'),
          repo.git.stash('list'))


if __name__ == "__main__":
    spp()
