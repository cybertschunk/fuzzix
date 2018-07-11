# -*- coding: utf-8 -*-
"""contains everything about protocols"""

from fuzzix.api.net.http.http_api import simple_http_processor
from fuzzix.api.net.dns.dns_api import simple_dns_processor


class Protocol:
    """represents a web protocol"""
    supported_protocols = []

    def __init__(self, proto_name, processor):
        self.proto_name = proto_name
        self.processor = processor
        Protocol.supported_protocols.append(proto_name.lower())

    @property
    def proto_name(self):
        """
        returns the name of the protocol instance
        return: the name of the protocol instance
        """
        return self.proto_name

    @property
    def processor(self):
        """
        returns the processor which can be used for this protocol instance
        return: the processsor for this protocol
        """
        return self.processor

    @proto_name.setter
    def proto_name(self, proto_name):
        """
        sets the name of the protocol
        return: None
        """
        self.proto_name = proto_name

    @processor.setter
    def processor(self, processor):
        """
        changes the processor
        return: None
        """
        self.processor = processor

    @staticmethod
    def is_valid_proto(name):
        """
        checks weither a given proto is supported
        (if there is a known protocol instance with this name)
        ignores cases
        return: True or False
        """
        return True if name.lower() in Protocol.supported_protocols else False


HTTP = Protocol('HTTP', simple_http_processor)
HTTPS = Protocol('HTTPS', simple_http_processor)
DNS = Protocol('DNS', simple_dns_processor)
