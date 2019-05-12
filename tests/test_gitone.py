#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `gitone` package."""

import pytest

from click.testing import CliRunner

from cli import camp_cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
