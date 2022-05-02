#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for element in reversed(my_list):
            print(f"{element:d}")
