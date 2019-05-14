# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``acamp()`` function."""
import click
from gitone.acamp import acamp


@click.command()
@click.argument("message", nargs=-1)
def acamp_cli(message: str) -> None:
    """Add and commit all changes.

    :param message: The commit message to be passed to ``acamp()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    acamp(" ".join(message)) if message else acamp()
