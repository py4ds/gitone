# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``acam()`` function."""
import click
from gitone.acam import acam


@click.command()
@click.argument("message", nargs=-1)
def acam_cli(message: str) -> None:
    """Add and commit all changes.

    :param message: The commit message to be passed to ``acam()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    acam(" ".join(message)) if message else acam()
