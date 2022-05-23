#!/usr/bin/python3
"""
Function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row_m_a in m_a:
        if type(row_m_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(row_m_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for num_a in row_m_a:
            if type(num_a) is not int and type(num_a) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for row_m_b in m_b:
        if type(row_m_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(row_m_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for num_b in row_m_b:
            if type(num_b) is not int and type(num_b) is not float:
                raise TypeError("m_b should contain only integers or floats")

    col_a = len(m_a[0])
    row_b = len(m_b)
    result = 0
    m_c = []

    if col_a == row_b:
        for row_a in range(len(m_a)):
            temp = []
            for col_b in range(len(m_b[0])):
                for num in range(col_a):
                    result += m_a[row_a][num] * m_b[num][col_b]
                temp.append(result)
                result = 0
            m_c.append(temp)
        return m_c
    else:
        raise ValueError("m_a and m_b can't be multiplied")
