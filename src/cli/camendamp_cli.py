# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``camendamp()`` function."""
import click
from gitone.camendamp import camendamp


@click.command()
@click.argument("message", nargs=-1)
def camendamp_cli(message: str) -> None:
    """Amend the previous commit with changes made to tracked files, then push.

    :param message: The commit message to be passed to ``camendamp()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    camendamp(" ".join(message)) if message else camendamp()
