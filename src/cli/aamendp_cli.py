# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``aamendp()`` function."""
import click
from gitone.aamendp import aamendp


@click.command()
@click.argument("message", nargs=-1)
def aamendp_cli(message: str) -> None:
    """Amend the previous commit by adding, committing, and pushing all files.

    :param message: The commit message to be passed to ``aamendp()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    aamendp(" ".join(message)) if message else aamendp()
