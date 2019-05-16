# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``camendam()`` function."""
import click
from gitone.camendam import camendam


@click.command()
@click.argument("message", nargs=-1)
def camendam_cli(message: str) -> None:
    """Amend the previous commit with changes made to tracked files.

    :param message: The commit message to be passed to ``camendam()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    camendam(" ".join(message)) if message else camendam()
