#!/usr/bin/python3
"""
Function that returns True if the object is exactly an instance ofi
the specified class otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance
    of the specified class
    otherwise False.
    """

    return type(obj) == a_class
