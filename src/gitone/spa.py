#!/usr/bin/env python
# -*- coding: utf-8 -*-
import git


def spa() -> None:
    """Stash local changes, pull with ``--rebase``, and apply local changes.

    :note: Use ``spa()`` if you try to pull with ``--rebase``
           and get an error that says::

               error: cannot pull with rebase: You have unstaged changes.
               error: please commit or stash them.

           With ``spa()`` the stash is preserved. Use ``git stash drop`` to
           remove the most recent stash.
    """

    repo = git.Repo(search_parent_directories=True)
    print(repo.git.stash('save'),
          repo.git.pull('--rebase'),
          repo.git.stash('apply'),
          repo.git.stash('list'))


if __name__ == "__main__":
    spa()
