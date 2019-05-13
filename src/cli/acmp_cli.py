# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``acmp()`` function."""
import click
from gitone.acmp import acmp


@click.command()
@click.argument("message", nargs=-1)
def acmp_cli(message: str) -> None:
    """Add and commit all changes, then push the commit.

    :param message: The commit message to be passed to ``acmp()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
           There is no need wrap the commit message in quotes.
    """
    acmp(" ".join(message)) if message else acmp()
