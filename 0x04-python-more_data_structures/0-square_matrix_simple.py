#!/usr/bin/python3
import sys
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for x in new_matrix:
        for i in range(0, len(new_matrix[0])):
            x[i] = x[i] ** 2
    return(new_matrix)
