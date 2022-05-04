#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        best = 0
        for val in a_dictionary:
            if a_dictionary[val] > best:
                best = a_dictionary[val]
        for key in a_dictionary.keys():
            if a_dictionary[key] == best:
                return key
    return None
