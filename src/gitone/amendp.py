#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git

from gitone.amend import amend


def amendp(message: Optional[str] = None) -> None:
    """Amend the previous commit with changes made to tracked files, then push.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    amend(message=message) if message else amend()
    repo = git.Repo(search_parent_directories=True)
    status, stdout, stderr = repo.git.push("--force",
                                           with_extended_output=True)
    print(f"Status: {status}, Output: {stdout}, Message: {stderr}.")


if __name__ == "__main__":
    amendp()
