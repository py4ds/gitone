# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``acamendm()`` function."""
import click
from gitone.acamendm import acamendm


@click.command()
@click.argument("message", nargs=-1)
def acamendm_cli(message: str) -> None:
    """Amend the previous commit by adding and committing all changes.

    :param message: The commit message to be passed to ``acamendm()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    acamendm(" ".join(message)) if message else acamendm()
