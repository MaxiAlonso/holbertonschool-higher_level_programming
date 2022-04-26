#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    str2 = ""
    for char in str:
        if count != n:
            str2 = str2 + char
        count += 1
    return(str2)
