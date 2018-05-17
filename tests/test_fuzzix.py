#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `fuzzix` package."""

import pytest
import unittest
import fuzzix.api


class ApiTest(unittest.TestCase):
    """tests the functions of the api module"""

    def test_core(self):
        """
        tests the function owned by api.core
        return: None
        """
        try:
            fuzzix.api.core.LOGGER.wtf('wtf')
            fuzzix.api.core.LOGGER.success('success')
            fuzzix.api.core.LOGGER.error('error')
            fuzzix.api.core.LOGGER.info('info')
            fuzzix.api.core.LOGGER.verbose('verbose')
        except BaseException as _e:
            self.fail('fuzzix.api.core.LOGGER not correctly working')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
