# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``camp()`` function."""
import click
from gitone.camp import camp


@click.command()
@click.argument("message", required=False, default="")
def camp_cli(message: str) -> None:
    """Add and commit changes made to tracked files and then push the commit.

    :param message: The commit message to be passed to ``camp()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
    """
    camp(message) if message else camp()
