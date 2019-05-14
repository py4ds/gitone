#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def acm(commit_message: Optional[str] = None) -> None:
    """Add and commit all changes."""

    repo = git.Repo()

    untracked = repo.untracked_files

    changed_file_lists = [
        [file.a_path
         for file in repo.index.diff(None).iter_change_type(change_type)]
        for change_type in ('D', 'M')
    ]

    if any(untracked + changed_file_lists):

        new = f"New files: {', '.join(untracked)}. " if untracked else ""

        prefixes = "Deleted files:", "Modified files:"

        deleted, modified = (
            f"{prefix} {', '.join(changed)}. " if changed else ""
            for prefix, changed in zip(prefixes, changed_file_lists)
        )

        print(f"Adding {', '.join(new + deleted + modified)}.",
              repo.git.add(untracked + changed_file_lists))

        if commit_message:
            print(repo.git.commit(untracked + changed_file_lists,
                                  message=commit_message))
        else:

            print(repo.git.commit(untracked + changed_file_lists,
                                  message=new + deleted + modified))

    else:
        print("There are no new, deleted, or modified files.")


if __name__ == "__main__":
    acm()
