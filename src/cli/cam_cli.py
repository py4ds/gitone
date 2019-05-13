# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the ``cam()`` function."""
import click
from gitone.cam import cam


@click.command()
@click.argument("message", required=False, default="")
def cam_cli(message: str) -> None:
    """Add and commit changes made to tracked files.

    :param message: The commit message to be passed to ``cam()``.
    :note: A commit message will be automatically generated
           if the ``message`` argument is not provided.
    """
    cam(message) if message else cam()
