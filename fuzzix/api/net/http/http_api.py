# -*- coding: utf-8 -*-
"""
implementation of the http protocol
"""
import urllib3
from bs4 import BeautifulSoup
from fuzzix.api.net.resource.url import URL
from fuzzix.api.core.resources.content import Content
urllib3.disable_warnings()


class _HTTPApi:
    """
    serves different functions for webcrawling
    """

    def __init__(self):
        self.__pool_manager__ = urllib3.PoolManager()

    def receive_url(self, url):
        """
        receives a given url
        attr url: the url to receive as URL
        return: the received content as Content together with the received content_type
        """
        if not isinstance(url, URL):
            raise ValueError('unsopported type for attribute url')

        response = self.__pool_manager__.request('GET', url.getURL())
        content = Content(url)
        content.set_status(response.status)
        content.set_content_type(response.getheaders()['Content-Type'])

        #check filetype
        if 'text' in response.getheaders()['Content-Type']:
            content.set_content(
                str(BeautifulSoup(response.data, 'html.parser')))
        else:
            content.set_content(response.data)
        return content


def grab_refs(content):
    """
    extracts most hyperlinks out of a given html document
    attribute content: a str encoded html document
    return: returns the extracted links as a list
    """
    results = []
    page = BeautifulSoup(content, 'html.parser')
    # divide in tags
    tags = page.find_all()
    # scanning src attributed
    for tag in tags:
        link = tag.get('src')
        if link is not None:
            results.append(link)
    # scanning href attribute
    for tag in tags:
        link = tag.get('href')
        if link is not None:
            results.append(link)
    return results


HTTP_API = _HTTPApi()


def simple_http_processor(content):
    """
    processes a given Content object. Reads the remote content on the given URL
    and stores it in the Content attribute
    attribute content: the content to proceed
    return: the proceeded content
    """
    if not isinstance(content, Content):
        raise ValueError(
            'expected type fuzzix.api.core.resources.Content for attribute Content'
        )

    target_url = content.getURL()
    proceeded_content = HTTP_API.receive_url(target_url)
    return proceeded_content
