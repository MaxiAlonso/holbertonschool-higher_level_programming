#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy() 
    for ridx, row in enumerate(matrix):
        for cidx, num in enumerate(row):
            new_matrix[ridx][cidx] = num ** 2
    return new_matrix
