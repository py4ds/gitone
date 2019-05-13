# -*- coding: utf-8 -*-

import click
from gitone.camp import camp


@click.command()
@click.argument("message", required=False, default="")
def camp_cli(message: str) -> None:
    """Command line interface (CLI) for the ``camp()`` function.

    :param message: The commit message to be passed to ``camp()``.
    """
    camp(message) if message else camp()
