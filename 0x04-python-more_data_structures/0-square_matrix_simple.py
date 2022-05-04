#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for ridx, row in enumerate(matrix):
        for cidx, num in enumerate(row):
            matrix[ridx][cidx] = num ** 2
    return matrix
