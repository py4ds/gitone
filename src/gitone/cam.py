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

    changed_file_lists = deleted_file_lists + modified_file_lists

    if any(changed_file_lists):

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

        print("Adding deleted and modified files.",
              repo.git.add("--update"))
        print("Deleted files:", deleted)
        print("Modified files:", modified_file_lists)

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
