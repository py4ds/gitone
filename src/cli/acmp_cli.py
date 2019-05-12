# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the acmp() function."""

import click
from gitone.acmp import acmp


@click.command()
@click.option("-m", "--message", "message")
def acmp_cli(message: str) -> None:
    acmp(message) if message else acmp()
