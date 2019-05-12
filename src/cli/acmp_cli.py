# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the acmp() function."""

import click
from gitone.acmp import acmp


@click.command()
def acmp_cli() -> None:
    acmp()
