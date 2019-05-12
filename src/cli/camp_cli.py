# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the camp() function."""

import click
from gitone.camp import camp


@click.command()
def camp_cli() -> None:
    camp()
