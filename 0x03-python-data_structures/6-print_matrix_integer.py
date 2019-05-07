#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix) > 1:
            for j in range(len(matrix[i])):
                if j < len(matrix[j]) - 1:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]))
        else:
            print()
