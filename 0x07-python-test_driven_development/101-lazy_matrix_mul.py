#!/usr/bin/python3
"""
Function that multiplies 2 matrices usin numpy library
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    """

    m_c = np.dot(m_a, m_b)
    return m_c
