#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def camendamp(message: Optional[str] = None) -> None:
    """Amend the previous commit with changes made to tracked files, then push.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    repo = git.Repo(search_parent_directories=True)

    print(repo.git.add("--update"))

    if message:
        print(repo.git.commit("--all", "--amend", message=message))

    else:
        print(repo.git.commit("--amend", "--reuse-message=HEAD"),
              repo.git.push("--force"))


if __name__ == "__main__":
    camendamp()
