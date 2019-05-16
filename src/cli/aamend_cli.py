# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``aamend()`` function."""
import click
from gitone.aamend import aamend


@click.command()
@click.argument("message", nargs=-1)
def aamend_cli(message: str) -> None:
    """Amend the previous commit by adding and committing all changes.

    :param message: The commit message to be passed to git commit command.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    aamend(" ".join(message)) if message else aamend()
