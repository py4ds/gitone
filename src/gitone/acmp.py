#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git

from gitone.acm import acm


def acmp(message: Optional[str] = None) -> None:
    """Add and commit all changes, then push the commit.

    :param message: The commit message to be passed to the git commit command.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
    """

    acm(message=message) if message else acm()
    repo = git.Repo(search_parent_directories=True)
    status, stdout, stderr = repo.git.push(extended_output = True)
    print(f"Status: {status}, Output: {stdout}, Message: {stderr}.")


if __name__ == "__main__":
    acmp()
