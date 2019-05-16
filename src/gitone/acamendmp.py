#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git

from gitone.acamendm import acamendm

def acamendmp(message: Optional[str] = None) -> None:
    """Amend the previous commit with any new changes, then push the commit.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    acamendm(message=message) if message else acamendm()
    repo = git.Repo(search_parent_directories=True)
    repo.git.push("--force"))


if __name__ == "__main__":
    acamendmp()
