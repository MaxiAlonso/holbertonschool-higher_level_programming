#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delkey_list = []
    for key, val in a_dictionary.items():
        if val == value:
            delkey_list.append(key)
    for key in delkey_list:
        del a_dictionary[key]
    return a_dictionary
