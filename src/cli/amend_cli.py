# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``amend()`` function."""
import click
from gitone.amend import amend


@click.command()
@click.argument("message", nargs=-1)
def amend_cli(message: str) -> None:
    """Amend the previous commit with changes made to tracked files.

    :param message: The commit message to be passed to git commit command.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    amend(" ".join(message)) if message else amend()
