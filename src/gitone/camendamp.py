#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git

from gitone.camendam import camendam


def camendamp(message: Optional[str] = None) -> None:
    """Amend the previous commit with changes made to tracked files, then push.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    camendam(message=message) if message else camendam()
    repo = git.Repo(search_parent_directories=True)
    repo.git.push("--force")
    repo.git.status()


if __name__ == "__main__":
    camendamp()
