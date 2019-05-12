#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git


def camp() -> None:
    repo = git.Repo()

    changed_file_lists = [
        [file.a_path
         for file in repo.index.diff(None).iter_change_type(change_type)]
        for change_type in ('D', 'M')
    ]

    if any(changed_file_lists):
        repo.git.add(changed_file_lists)

        prefixes = "Deleted files:", "Modified files:"

        deleted, modified = (
            f"{prefix} {', '.join(changed_files)}. " if changed_files else ""
            for prefix, changed_files in zip(prefixes, changed_file_lists)
        )

        print(repo.git.commit(changed_file_lists, message=deleted + modified),
              repo.git.push())

if __name__ == "__main__":
    camp()
