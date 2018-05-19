# -*- coding: utf-8 -*-
"""
providing high-level core functionalities for fuzzix
"""
import os
import configparser
from coloredlogger import ColoredLogger

#logger for the fuzzxi suite
LOGGER = ColoredLogger(name="FUZZIX")


class Settings:
    """can read, write and maintain settings"""

    def __init__(self):
        self.__config__ = {}

    def read_config(self, path):
        """
        reads the config file located on the given locaton using configparser
        attribute path: the path to the config file as str
        raises: ValueError, if no config settings could be found at the given location
        return: None
        """
        config_file = configparser.ConfigParser()
        config_file.read(path)
        if len(config_file.sections()) <= 0:
            raise ValueError("given config empty or not existend")
        for section in config_file.sections():
            for key in config_file[section]:
                self.__config__[section + "/" +
                                key] = config_file[section][key]

    def write_config(self, path, overwrite_config=True):
        """
        writes the current settings to the given location using configparser
        attribute path: the path to the config file as str
        attribute overwrite_config: Overwrite an existing config
        raises: ValueError, if the given path is invalid or writing failes
        raises: ValueError, if overwriting is turned off, but there is already a
        file given at the given location
        return: None
        """
        if os.path.exists(path) and not overwrite_config:
            raise ValueError('can\'t overwrite config in this configuration')

        #exporting settings to a configparser instance
        config_p = configparser.ConfigParser()
        for key in self.__config__:
            if '/' in key:
                section, sectionkey = key.split('/')
                if not config_p.has_section(section):
                    config_p.add_section(section)

                config_p[section][sectionkey] = self.__config__[key]
            else:
                raise ValueError('key ' + key + " has no section")

        #write settings to file
        try:
            with open(path, 'w') as config_file:
                config_p.write(config_file)
        except (OSError, IOError) as error:
            raise ValueError('couldn\'t write to given path ' + path + " " +
                             str(error))
        return None

    def write_attribute(self, key, value):
        """
        writes an given attribute to the config file
        attribute key: the key for the attribute
        attribute value: the value to store
        raises: ValueError if the key hasn't the right format
        return: None
        """
        if key.count('/') != 1:
            raise ValueError('section/key not correctly specified')

        self.__config__[key] = value

    def read_attribute(self, key, default):
        """
        reads an attribute from the config
        attribute key: the key to read
        attribute default: the default value, which will be returned,
        if the key couldn't be found in the config
        return: either the default-value or the value of the key in the config
        """
        if key in self.__config__:
            return self.__config__[key]
        else:
            #logging waring
            LOGGER.wtf("key " + key +
                       " couldn't be found, returning default value " +
                       default + " instead")
            return default

    def __str__(self):
        """
        return: The actual config as str
        """
        result = ''
        for key in self.__config__:
            result = result + key + " : " + self.__config__[key]
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__config__ == other.__config__
        else:
            return False