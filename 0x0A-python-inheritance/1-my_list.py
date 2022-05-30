#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """
    Class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """

        print(sorted(self))
