# -*- coding: utf-8 -*-

import click
from gitone.cam import cam


@click.command()
@click.argument("message", required=False, default="")
def cam_cli(message: str) -> None:
    """Command line interface (CLI) for the ``cam()`` function.

    :param message: The commit message to be passed to ``cam()``.
    """
    cam(message) if message else cam()
