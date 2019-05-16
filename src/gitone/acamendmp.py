#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def acamendmp(message: Optional[str] = None) -> None:
    """Amend the previous commit with any new changes, then push the commit.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    repo = git.Repo(search_parent_directories=True)

    print(repo.git.add("--all"))

    if commit_message:
        print(repo.git.commit("--all", "--amend", message=commit_message))

    else:
        print(repo.git.commit("--amend", "--reuse-message=HEAD"),
              repo.git.push("--force"))


if __name__ == "__main__":
    acamendmp()