#!/usr/bin/python3
"""
Class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt Class
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
