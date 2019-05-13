# -*- coding: utf-8 -*-
import click
from gitone.acmp import acmp


@click.command()
@click.argument("message", required=False, default="")
def acmp_cli(message: str) -> None:
    """Command line interface (CLI) for the ``acmp()`` function.

    :param message: The commit message to be passed to ``acmp()``.
    """
    acmp(message) if message else acmp()
