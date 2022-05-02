#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        element = 0
        for element in range(len(row)):
            if element == len(row) - 1:
                print(f"{row[element]}", end="")
            else:
                print(f"{row[element]}", end=" ")
        print()
