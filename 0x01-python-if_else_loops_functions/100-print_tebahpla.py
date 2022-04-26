#!/usr/bin/python3
for alph in reversed(range(97, 123)):
    if alph % 2 != 0:
        alph -= 32
    print("{}".format(chr(alph)), end="")
