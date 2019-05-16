#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def cam(message: Optional[str] = None) -> None:
    """Add and commit changes made to tracked files.

    :param message: The commit message to be passed to the git commit command.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
    """

    repo = git.Repo(search_parent_directories=True)

    diffs = repo.index.diff(None), repo.index.diff(repo.head.commit)

    changed_file_lists = [
        [file.a_path
         for file in diff.iter_change_type(change_type)]
        for diff, change_type in zip(diffs, ('D', 'M'))
    ]

    print(changed_file_lists)

    if any(changed_file_lists):

        prefixes = "Deleted files:", "Modified files:"

        deleted, modified = (
            f"{prefix} {', '.join(changed)}. " if changed else ""
            for prefix, changed in zip(prefixes, changed_file_lists)
        )

        print("Adding deleted and modified files.",
              repo.git.add("--update"))

        if message:
            print(repo.git.commit(changed_file_lists,
                                  message=message))

        else:

            print(repo.git.commit(changed_file_lists,
                                  message=deleted + modified))

    else:
        print("There are no deleted or modified files.")


if __name__ == "__main__":
    cam()
