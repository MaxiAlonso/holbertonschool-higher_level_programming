#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        tup = (0, None)
    else:
        tup = (len(sentence), sentence[0])
    return tup
