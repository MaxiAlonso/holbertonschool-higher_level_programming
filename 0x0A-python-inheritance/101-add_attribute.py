#!/usr/bin/python3
"""
Function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """
    add a new attributei
    """

    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
