# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``acm()`` function."""
import click
from gitone.acm import acm


@click.command()
@click.argument("message", nargs=-1)
def acm_cli(message: str) -> None:
    """Add and commit all changes.

    :param message: The commit message to be passed to ``acm()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    acm(" ".join(message)) if message else acm()
