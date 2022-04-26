#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        start = str[:n]
        end = str[n+1:]
        return(start+end)
    return(str);
