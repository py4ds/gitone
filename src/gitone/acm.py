#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

import git


def acm(message: Optional[str] = None) -> None:
    """Add and commit all changes.

    :param message: The commit message to be passed to the git commit command.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
    """

    repo = git.Repo(search_parent_directories=True)

    untracked = repo.untracked_files

    diffs = repo.index.diff(None), repo.index.diff(repo.head.commit)

    deleted_file_lists = [
        [file.a_path for file
         in diff.iter_change_type('D')]
        for diff in diffs
    ]

    modified_file_lists = [
        [file.a_path for file
         in diff.iter_change_type('M')]
        for diff in diffs
    ]

    changed_file_lists = untracked + deleted_file_lists + modified_file_lists

    if any(changed_file_lists):

        new = f"New files: {', '.join(untracked)}. " if untracked else ""

        deleted = [
            f"Deleted files: {', '.join(deleted_file_list)}. "
            if deleted_file_lists else ""
            for deleted_file_list in deleted_file_lists
        ]

        modified = [
            f"Modified files: {', '.join(modified_file_list)}. "
            if modified_file_list else ""
            for modified_file_list in modified_file_lists
        ]

        print(f"Adding new, deleted, and modified files.",
              repo.git.add("--all"))

        if message:
            print(repo.git.commit(changed_file_lists,
                                  message=message))
        else:

            print(repo.git.commit(changed_file_lists,
                                  message=new + deleted + modified))

    else:
        print("There are no new, deleted, or modified files.")


if __name__ == "__main__":
    acm()
