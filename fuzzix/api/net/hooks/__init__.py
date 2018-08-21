# -*- coding: utf-8 -*-
from fuzzix.api.core.resources import _Structure
from fuzzix.api.net.resource.url import URL


class SearchResult(_Structure):
    """stores all important attributes of a search result"""

    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    @property
    def url(self):
        """
        returns the url of the search result
        return: the url of the search result
        """
        return self.url

    @property
    def title(self):
        """
        returns the title of the search result
        return: the title of the search result
        """
        return self.title

    @property
    def description(self):
        """
        returns the description of the search result
        return: the description of the search result
        """
        return self.description

    @url.setter
    def url(self, url):
        """
        sets the url of the search result to a new url
        attr url: The url to store as URL
        return: None
        """
        if not isinstance(url, URL):
            raise ValueError('not supported type for attribute url')
        self.url = url

    @title.setter
    def title(self, title):
        """
        sets the title of the search result to a new title
        attr title: the title to store as str
        return: None
        """
        if not isinstance(title, str):
            raise ValueError('not supported type for attribute title')
        self.title = title

    @description.setter
    def description(self, description):
        """
        sets the description of a search result to a new one
        attr description: the new description
        return: None
        """
        self.description = description
