# -*- coding: utf-8 -*-
"""
providing high-level core functionalities for fuzzix
"""


class _Structure:
    """abstract base class for all structures"""

    def __init__(self):
        pass

    @staticmethod
    def from_node(node):
        """
        creates an object out of the given node -> must be overwritten by the sub-classes
        attribute node: the node to be used
        return: the created object
        """
        raise NotImplementedError("not implemented in base class Structure")

    def to_node(self):
        """
        creates a node containing all attributes of the object,
        so that the exact equal object can be created by from_node
        return: the created node
        """
        raise NotImplementedError("not implemented in base class Structure")
