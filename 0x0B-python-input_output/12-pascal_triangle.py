#!/usr/bin/python3
"""
Function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    final_list = []

    if n > 0:
        for lists in range(1, n + 1):
            new_list = []
            for element in range(1, lists + 1):
                if element == 1 or element == lists:
                    new_list.append(1)
                else:
                    sum_list = final_list[lists - 2]
                    result = sum_list[element - 2] + sum_list[element - 1]
                    new_list.append(result)
            final_list.append(new_list)

    return final_list
