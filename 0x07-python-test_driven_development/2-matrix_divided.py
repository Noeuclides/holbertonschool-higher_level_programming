#!/usr/bin/python3
def matrix_divided(matrix, div):
    new = [[]]
    try:
        new = [[round(j/div, 2) for j in i] for i in matrix]
        return(new)
    except TypeError:
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    except TypeError:
        raise TypeError("Each row of the matrix must have the same size")
    except TypeError:
        raise TypeError("div must be a number")
    except ZeroDivisionError:
        raise TypeError("division by zero")
