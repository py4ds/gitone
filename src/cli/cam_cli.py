# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the acmp() function."""

import click
from gitone.cam import cam


@click.command()
@click.option("-m", "--message", "message")
def cam_cli(message: str) -> None:
    cam(message) if message else cam()
