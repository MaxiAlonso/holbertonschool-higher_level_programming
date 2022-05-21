#!/usr/bin/python3
"""
Function that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    for height in range(size):
        for width in range(size):
            print("#", end="")
        print()
