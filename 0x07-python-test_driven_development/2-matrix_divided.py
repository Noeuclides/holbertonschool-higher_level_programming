#!/usr/bin/python3
"""
this is a module
that takes a matrix
and operates it with an integer
"""


def matrix_divided(matrix, div):
    """
    function that divides the elements of a matrix with an integer
    """
    new = [[]]
    l = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    for i in matrix:
        if len(i) != l:
            raise TypeError("Each row of the matrix must have the same size")
    new = [[round(j/div, 2) for j in i] for i in matrix]
    return(new)
