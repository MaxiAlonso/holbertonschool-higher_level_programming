#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if roman_string is not None:
        for idx, char in enumerate(roman_string):
            ni = idx + 1  # inext idx
            if char == "I":
                if ni < len(roman_string):
                    if roman_string[ni] == "V" or roman_string[ni] == "X":
                        num -= 1
                    else:
                        num += 1
                else:
                    num += 1
            if char == "V":
                num += 5
            if char == "X":
                if ni < len(roman_string):
                    if roman_string[ni] == "L" or roman_string[ni] == "C":
                        num -= 10
                    else:
                        num += 10
                else:
                    num += 10
            if char == "L":
                num += 50
            if char == "C":
                if ni < len(roman_string):
                    if roman_string[ni] == "D" or roman_string[ni] == "M":
                        num -= 100
                    else:
                        num += 100
                else:
                    num += 100
            if char == "D":
                num += 500
            if char == "M":
                num += 1000
    return num
