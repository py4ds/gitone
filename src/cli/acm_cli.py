# -*- coding: utf-8 -*-
import click
from gitone.acm import acm


@click.command()
@click.argument("message", required=False, default="")
def acm_cli(message: str) -> None:
    """Command line interface (CLI) for the ``acm()`` function.

    :param message: The commit message to be passed to ``acm()``.
    """
    acm(message) if message else acm()
