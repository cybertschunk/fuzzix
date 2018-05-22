# -*- coding: utf-8 -*-
"""contains all classes about URLs"""

from fuzzix.api.core.resources import _Structure


class _AbstractURL(_Structure):
    """
    abstract base class for all types of URLs
    """

    def __init__(self, url):
        pass


class URL(_AbstractURL):
    def __init__(self, url):
        pass


class BaseURL(_AbstractURL):
    def __init__(self, url):
        pass


class PathURL(_AbstractURL):
    pass