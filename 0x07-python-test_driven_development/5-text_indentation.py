#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: "." "?" ":"
    """

    charlist = [".", "?", ":"]
    spaces = "\n\n"
    skipspace = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        if skipspace == 1:
            skipspace = 0
            continue
        print(char, end="")
        if char in charlist:

            print(spaces, end="")
            skipspace = 1
