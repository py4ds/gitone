#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git

from gitone.aamend import aamend

def aamendp(message: Optional[str] = None) -> None:
    """Amend the previous commit with any new changes, then push the commit.

    :param message: The commit message to be passed to the git commit command.
    :note: The previous commit message will be reused
           if the ``message`` argument is not provided.
    """

    aamend(message=message) if message else aamend()
    repo = git.Repo(search_parent_directories=True)
    print(repo.git.push("--force", with_extended_output=True)[2])


if __name__ == "__main__":
    aamendp()
