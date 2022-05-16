#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as Error:
        print("Exception: {}".format(Error), file=sys.stderr)
        return None
