#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def caam(commit_message: Optional[str] = None) -> None:
    """Amend the previous commit with new changes made to tracked files."""

    repo = git.Repo()

    print(repo.git.add("--all"))

    if commit_message:
        print(repo.git.commit("--all", "--amend", message=commit_message))

    else:
        print(repo.git.commit("--amend", "--reuse-message=HEAD"))


if __name__ == "__main__":
    caam()
