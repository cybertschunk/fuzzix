# -*- coding: utf-8 -*-
"""Tests for `fuzzix` package."""

import unittest
from fuzzix import api
from fuzzix.api.core.settings import Settings
from fuzzix.api.core.resources import _Structure
from fuzzix.api.core.resources.content import Content


class CoreTest(unittest.TestCase):
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
        except BaseException as error:
            self.fail('fuzzix.api.core.LOGGER not correctly working ' +
                      str(error))

    def test_core_config(self):
        """
        tests the Settings class provided by api.core
        return: None
        """
        try:
            #basic testing
            default_path = 'config/config.ini'
            settings = api.core.settings.Settings()
            settings.read_config(default_path)
            self.assertEqual(
                settings.read_attribute('abc', 'abc'),
                'abc',
                msg=
                'fuzzix.api.core.Config is not correctly handling not known keys'
            )
            self.assertEqual(
                settings.read_attribute('WORDLISTS/directories', ''),
                'worlists/directories.txt',
                msg=
                'api.core.Settings is not returning the right attribute for the given key'
            )

            with self.assertRaises(
                    ValueError,
                    msg=
                    'api.core.Settings is reading settings from not existing paths'
            ):
                settings.read_config('not existing path', )

            # test writing
            with self.assertRaises(
                    ValueError,
                    msg=
                    'api.core.Settings is overwriting existing config allthough it was told not to'
            ):
                settings.write_config(default_path, overwrite_config=False)

            with self.assertRaises(
                    ValueError,
                    msg='api.core.Settings is writing in not existing dirs'):
                settings.write_config('NOT_EXIST_DIR/config.ini')

            settings.write_config('config/config2.ini')

            # test equality
            settings2 = api.core.settings.Settings()
            self.assertNotEqual(
                settings,
                settings2,
                msg='not equal settings classes are apparently equal')
            settings2.read_config('config/config2.ini')
            self.assertEqual(
                settings,
                settings2,
                msg=
                'equal settings classes are apparently not equal or importing/exporting config to file is not correctly handled'
            )

            #test integrity
            self.assertEqual(
                settings.read_attribute('WORDLISTS/directories', ''),
                'worlists/directories.txt',
                msg='settings not correctly reading out settings attributes')
            self.assertEqual(
                settings2.read_attribute(
                    'WORDLISTS/directories',
                    'settings2 not correctly reading out settings attributes'),
                'worlists/directories.txt')

        except BaseException as error:
            self.fail('fuzzix.api.core.Config not correctly working ' +
                      str(error))

    def test_core_structure(self):
        """
        tests the class fuzzix.api.core.resources._Structure
        return: None
        """
        structure = _Structure("test")
        try:
            structure.to_node()
            structure.from_node(None)
            self.fail('_Structure isn\'t an abstract basis class')
        except NotImplementedError as _e:
            pass
