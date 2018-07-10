# -*- coding: utf-8 -*-
import dns.resolver


class _DNSApi:
    """class to perform dns querys"""
    NAME_SERVERS = {
        'LEVEL3': ('209.244.0.3', '209.244.0.4'),
        'Verisign': ('64.6.64.6', '64.6.65.6'),
        'Google': ('8.8.8.8', '8.8.4.4'),
        'Quad9': ('9.9.9.9', '149.112.112.112'),
        'OpenDNS': ('208.67.222.222', '208.67.220.220'),
        'Cloudflare': ('1.1.1.1', '1.0.0.1'),
        'UncensoredDNS': ('91.239.100.100', '89.233.43.71')
    }

    def __init__(self, name_server='Cloudflare'):
        self.__resolver__ = dns.resolver.Resolver()

        #set nameserver
        if name_server not in self.NAME_SERVERS:
            raise ValueError('unsupported nameserver given')
        self.__resolver__.nameservers = self.NAME_SERVERS[name_server]

    def raw_lookup(self, querysubject, query):
        """
        querys the dns server
        attr querysubject: the subject of the query
        attr query: the query type
        return the result of the querys
        """
        if not isinstance(querysubject, str) or not isinstance(query, str):
            raise ValueError('given arguments have unsupported types')
        return self.__resolver__.query(querysubject, query)

    def ipv4_lookup(self, querysubject):
        """
        querys the A record of the querysubject
        attr querysubject: the subject of the query
        return: the result of the query
        """
        return self.raw_lookup(querysubject, 'A')

    def ipv6_lookup(self, querysubject):
        """
        querys the AAAA record of the querysubject
        attr querysubject: the subject of the query
        return: the result of the query
        """
        return self.raw_lookup(querysubject, 'AAAA')

    def mx_lookup(self, querysubject):
        """
        querys the mx record of the querysubject
        attr querysubject: the subject of the query
        return: the result of the query
        """
        return self.raw_lookup(querysubject, 'MX')


DNS_API = _DNSApi()
