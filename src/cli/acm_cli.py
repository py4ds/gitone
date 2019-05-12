# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the acmp() function."""

import click
from gitone.acm import acm


@click.command()
@click.option("-m", "--message", "message")
def acm_cli(message: str) -> None:
    acm(message) if message else acm()
