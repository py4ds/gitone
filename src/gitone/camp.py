#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def camp(commit_message: Optional[str] = None) -> None:
    """Add and commit changes made to tracked files, then push the commit."""

    repo = git.Repo()

    changed_file_lists = [
        [file.a_path
         for file in repo.index.diff(None).iter_change_type(change_type)]
        for change_type in ('D', 'M')
    ]

    if any(changed_file_lists):

        prefixes = "Deleted files:", "Modified files:"

        deleted, modified = (
            f"{prefix} {', '.join(changed)}. " if changed else ""
            for prefix, changed in zip(prefixes, changed_file_lists)
        )

        print(f"Adding {', '.join(deleted + modified}.",
              repo.git.add(changed_file_lists))

        if commit_message:
            print(repo.git.commit(changed_file_lists,
                                  message=commit_message),
                  repo.git.push(),
                  f"\nPushing to {', '.join(repo.remote().urls)}.")

        else:

            print(repo.git.commit(changed_file_lists,
                                  message=deleted + modified),
                  repo.git.push(),
                  f"\nPushing to {', '.join(repo.remote().urls)}.")

    else:
        print("There are no deleted or modified files.")


if __name__ == "__main__":
    camp()
