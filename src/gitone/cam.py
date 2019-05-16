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

    def get_changes(change_type):
        for diff in [repo.index.diff(None), repo.index.diff(repo.head.commit)]:
            for file in diff.iter_change_type(change_type):
                yield file.a_path

    dellist, modlist = (list(get_changes(c_type)) for c_type in ('D', 'M'))
    changed_list = dellist + modlist

    if any(changed_list):

        deleted = f"Deleted files: {', '.join(dellist)}. " if dellist else ""
        modified = f"Modified files: {', '.join(modlist)}." if modlist else ""

        auto_message = deleted + modified

        print(repo.git.add("--update"))

        if message:
            print(repo.git.commit(changed_list, message=message))

        else:
            print(repo.git.commit(changed_list, message=auto_message))

    else:
        print("There are no deleted or modified files.")


if __name__ == "__main__":
    cam()
