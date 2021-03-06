# -*- coding: utf-8 -*-
"""Tests for `fuzzix` package."""

import unittest
from fuzzix import api
from fuzzix.api.core.settings import Settings
from fuzzix.api.core.resources import _Structure
from fuzzix.api.core.resources.content import Content
from fuzzix.api.net.resource.url import URL
from fuzzix.api.net.dns.dns_api import DNS_API, extract_query_results


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
            settings = Settings()
            settings2 = Settings()
            settings.read_config(default_path)
            self.assertEqual(
                settings.read_attribute('abc', 'abc'),
                'abc',
                msg=
                'fuzzix.api.core.Config is not correctly handling not known keys'
            )

            # test reading
            self.assertEqual(
                settings.read_attribute('WORDLISTS/directories', ''),
                'worlists/directories.txt',
                msg=
                'api.core.Settings is not returning the right attribute for the given key'
            )

            # test reading from file
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

            settings.write_attribute('tests/test', 'abc')
            self.assertNotEqual(
                settings,
                settings2,
                msg='key not correctly stored by settings attribute')

            self.assertEqual(
                'abc',
                settings.read_attribute('tests/test', ''),
                msg='key not correctly stored by settings attribute')

            with self.assertRaises(
                    ValueError,
                    msg='malformed keys are not correctly handled'):
                settings.write_attribute('TEST', 'TEST')

            # test writing to file
            with self.assertRaises(
                    ValueError,
                    msg='api.core.Settings is writing in not existing dirs'):
                settings.write_config('NOT_EXIST_DIR/config.ini')

            with self.assertRaises(
                    ValueError,
                    msg='malformed keys are not correctly handled'):
                settings.__config__['TEST'] = 'TEST'
                settings.write_config('config/config2.ini')

            settings = Settings()
            settings.read_config('config/config.ini')
            settings.write_config('config/config2.ini')

            # test equality
            tmp_str = "abc"
            self.assertNotEqual(
                settings,
                tmp_str,
                msg=
                'settings attribute is apparently equal to a string instance')

            self.assertNotEqual(
                settings,
                settings2,
                msg='not equal settings classes are apparently equal')

            settings2.read_config('config/config2.ini')
            self.assertEqual(
                settings,
                settings2,
                msg=
                'equal settings classes are apparently not equal or importing/'\
                'exporting config to file is not correctly handled'
            )

            # test integrity
            self.assertEqual(
                settings.read_attribute('WORDLISTS/directories', ''),
                'worlists/directories.txt',
                msg='settings not correctly reading out settings attributes')

            self.assertEqual(
                settings2.read_attribute(
                    'WORDLISTS/directories',
                    'settings2 not correctly reading out settings attributes'),
                'worlists/directories.txt')

            # test delitem
            settings.write_attribute('tests/test', 'abc')
            with self.assertRaises(
                    ValueError,
                    msg='settings class is deleting not existing keys'):
                settings.del_attribute('tests/NOT_EXISTING')

            settings.del_attribute('tests/test')
            self.assertEqual(
                settings, settings2, msg='keys are not correctly deleted')

            # test printing
            print(settings)

        except BaseException as error:
            self.fail('fuzzix.api.core.Config not correctly working ' +
                      str(error))

    def test_core_resources_structure(self):
        """
        tests the class fuzzix.api.core.resources._Structure
        return: None
        """
        structure = _Structure()
        try:
            structure.to_node()
            self.fail('_Structure isn\'t an abstract basis class')
        except NotImplementedError as _e:
            pass
        try:
            structure.from_node(None)
            self.fail('_Structure isn\'t an abstract basis class')
        except NotImplementedError as _e:
            pass

    def test_core_resources_content(self):
        """
        tests the class fuzzix.api.core.resources.Content
        return: None
        """
        try:
            test_url = URL(
                'https://raw.githubusercontent.com/cybertschunk/fuzzix/master/tests/web/index.html'
            )
            test_content = Content(test_url)
        except BaseException as error:
            self.fail(
                'fuzzix.api.core.resources.Content not correctly working ' +
                str(error))


class NetTest(unittest.TestCase):
    """tests fuzzix.api.net"""

    def test_net_dns_dns_api(self):
        """
        tests the fuzzix.api.net.dns.dns_api
        """
        pass
