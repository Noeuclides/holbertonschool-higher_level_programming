#!/usr/bin/python3
"""
module that use numpy
to multiply
two number
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies two numbers
    """
    a = numpy.array(m_a)
    b = numpy.array(m_a)
    return(a.dot(b))
