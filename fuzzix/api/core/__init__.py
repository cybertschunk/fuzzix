# -*- coding: utf-8 -*-
"""
providing high-level core functionalities for fuzzix
"""
import configparser
from coloredlogger import ColoredLogger
LOGGER = ColoredLogger(name="FUZZIX")


class Settings:
    """can read, write and maintain settings"""

    def __init__(self):
        self.config = {}

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
                self.config[section + "/" + key] = config_file[section][key]

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
        return None

    def write_attribute(self, key, value):
        """
        writes an given attribute to the config file
        attribute key: the key for the attribute
        attribute value: the value to store
        return: None
        """
        self.config[key] = value

    def read_attribute(self, key, default):
        """
        reads an attribute from the config
        attribute key: the key to read
        attribute default: the default value, which will be returned, 
        if the key couldn't be found in the config
        return: either the default-value or the value of the key in the config
        """
        if key in self.config:
            return self.config[key]
        else:
            #logging waring
            LOGGER.wtf("key " + key +
                       " couldn't be found, returning default value " +
                       default + " instead")
            return default

    def __str__(self):
        """
        prints the actual config
        return: None
        """
        result = ''
        for key in self.config:
            result = result + key + " : " + self.config[key]
        return result
