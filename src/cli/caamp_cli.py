# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``caamp()`` function."""
import click
from gitone.caamp import caamp


@click.command()
@click.argument("message", nargs=-1)
def caamp_cli(message: str) -> None:
    """Add and commit all changes.

    :param message: The commit message to be passed to ``caamp()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    caamp(" ".join(message)) if message else caamp()
