#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `fuzzix` package."""

import pytest
import unittest
from fuzzix import fuzzix
from fuzzix import api
from fuzzix.api import core


class ApiTest(unittest.TestCase):
    """tests the functions of the api module"""

    def test_core(self):
        """
        tests the function owned by api.core
        return: None
        """
        try:
            api.core.LOGGER.wtf('wtf')
            api.core.LOGGER.success('success')
            api.core.LOGGER.error('error')
            api.core.LOGGER.info('info')
            api.core.LOGGER.verbose('verbose')
        except BaseException as _e:
            self.fail('fuzzix.api.core.LOGGER not correctly working')
