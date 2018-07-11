# -*- coding: utf-8 -*-
"""contains all classes about URLs"""
from urllib.parse import urlparse, urljoin, urlunparse
from fuzzix.api.core.resources import _Structure


class _AbstractURL(_Structure):
    """abstract base class for all types of URLs"""

    def __init__(self):
        super(_AbstractURL, self).__init__()


class URL(_AbstractURL):
    """represents an URL, contains an instance of a BaseURL and a PathURL"""

    def __init__(self, url):
        super(URL, self).__init__()

    @staticmethod
    def is_valid_url(url):
        """
        checks weither a given URL is valid
        attribute url: the url to check as str
        return: True if URL is valid, otherwise False
        """
        urlparts = urlparse(url)
        if urlparts.netloc and urlparts.scheme:
            return True
        return False


class _BaseURL(_AbstractURL):
    """contains the target host, port, proto, username and password of the URL"""

    def __init__(self, url):
        pass


class _PathURL(_AbstractURL):
    """contains the target path, params, query and fragments of the URL"""

    def __init__(self, path, params, query, fragments):
        if not isinstance(path, str) or not isinstance(
                params, str) or not isinstance(query, str) or not isinstance(
                    fragments, str):
            raise ValueError('One of the arguments has an unsupported type')

        self.path = path
        self.params = params
        self.query = query
        self.fragments = fragments
