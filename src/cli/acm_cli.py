# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the acmp() function."""

import click
from gitone.acm import acm


@click.command()
def acm_cli() -> None:
    acm()
