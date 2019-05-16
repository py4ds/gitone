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

    def get_changes(change_type):
        for diff in [repo.index.diff(None), repo.index.diff(repo.head.commit)]:
            for file in diff.iter_change_type(change_type):
                yield file.a_path

    new_list = repo.untracked_files
    # Not sure why deleted files have change_type == 'A'...
    del_list = list(set(get_changes('A'))) + list(set(get_changes('D')))
    mod_list = list(set(get_changes('M')))
    changed = new_list + del_list + mod_list

    if any(changed):
        new_str = f"New files: {', '.join(new_list)}. " if new_list else ""
        del_str = f"Deleted files: {', '.join(del_list)}. " if del_list else ""
        mod_str = f"Modified files: {', '.join(mod_list)}." if mod_list else ""

        print(repo.git.add("--all"))

        if message:
            print(repo.git.commit(changed, message=message))

        else:
            print(repo.git.commit(changed, message=new_str + del_str + mod_str))

    else:
        print("There are no new, deleted, or modified files.")


if __name__ == "__main__":
    acm()
