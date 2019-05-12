# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the camp() function."""

import click
from gitone.camp import camp


@click.command()
@click.option("-m", "--message", "message")
def camp_cli(message: str) -> None:
    camp(message) if message else camp()
