#!/usr/bin/python3
"""
module that use numpy
to multiply
two number
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies two numbers
    """
    a = np.array(m_a)
    b = np.array(m_a)
    return(a.dot(b))
