#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_slip_proactive
----------------------------------

Tests for `slip_proactive` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from slip_proactive import slip_proactive
from slip_proactive import cli


class TestSlipProactive(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'slip_proactive.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
