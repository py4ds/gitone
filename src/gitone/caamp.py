#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def caamp(commit_message: Optional[str] = None) -> None:
    """Amend the previous commit and push new changes made to tracked files."""

    repo = git.Repo()

    print(repo.git.add("--update"))

    if commit_message:
        print(repo.git.commit("--all", "--amend", message=commit_message))

    else:
        print(repo.git.commit("--amend", "--reuse-message=HEAD"),
              repo.git.push("--force"))


if __name__ == "__main__":
    caamp()
