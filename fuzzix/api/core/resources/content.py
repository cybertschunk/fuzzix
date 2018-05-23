# -*- coding: utf-8 -*-

from fuzzix.api.core.resources import _Structure
from fuzzix.api.net.resource.url import URL


class Content(_Structure):
    """
    a class to represent content on a remote host
    """

    def __init__(self, url):
        if not isinstance(url, URL):
            raise ValueError("invalid type for attribute url")

        self.url = url
        self.size = 0
        self.content = ""
        self.content_type = ""
        self.processor = None
        self.status = 0
        super(Content, self).__init__()

    def get_url(self):
        """
        returns the url pointing to the content
        return: the url pointing to the content
        """
        return self.url

    def get_size(self):
        """
        returns the size of the content
        return: size of the content
        """
        return len(self.get_content())

    def get_content(self):
        """
        returns the content itself
        return: the content itself
        """
        return self.content

    def get_status(self):
        """
        returns the status of the content
        return: the status of the content
        """
        return self.status

    def get_content_type(self):
        """
        returns the type of the content
        return: the type of the content
        """
        return self.content_type

    def get_processor(self):
        """
        returns the processor for the content found on the given url,
        the processed content will be than stored at self.content
        return: the processor fot the content found on the given url
        """
        return self.processor

    def set_status(self, status):
        """
        sets the status of the stored content
        attr status: the status to set
        return: None
        """
        self.status = status

    def set_content(self, content):
        """
        sets the content itself
        attr content: the content to store
        return: None
        """
        self.content = content

    def set_content_type(self, content_type):
        """
        sets the type of the stored content
        attr contentType: the type to store
        return: None
        """
        self.content_type = content_type

    def set_processor(self, processor):
        """
        sets the processor for the content found on the given url
        attr processor: the processor to set
        return: None
        """
        self.processor = processor

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.content == other.content and self.content_type == other.content_type \
            and self.status == other.status and self.processor == other.processor
        else:
            return False
