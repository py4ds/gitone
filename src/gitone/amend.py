#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def amend(message: Optional[str] = None) -> None:
    """Amend the previous commit with changes made to tracked files.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    repo = git.Repo(search_parent_directories=True)

    print(repo.git.add("--update"))

    if message:
        print(repo.git.commit("--all", "--amend", message=message))

    else:
        print(repo.git.commit("--amend", "--reuse-message=HEAD"))


if __name__ == "__main__":
    amend()
