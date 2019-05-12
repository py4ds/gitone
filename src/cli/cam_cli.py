# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the acmp() function."""

import click
from gitone.cam import cam


@click.command()
def cam_cli() -> None:
    cam()
