#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    
    new_list = []

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for row in matrix:
            if row is not None:
                lenrow = len(row)
            else:
                lenrow = None
            temp_list = [] 
            for number in row:
                if type(number) is not int and type(number) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                if len(matrix[0]) != lenrow:
                    raise TypeError("Each row of the matrix must have the same size")
                temp_list.append((round((number / div), 2)))
            new_list.append(temp_list)
        return new_list
