"""
Matrix

Code from Chapter 4 of Data Science from Scratch
"""
import math
from vector import dot


def rows(A):
    return len(A)

def cols(A):
    return A.shape[1] if hasattr(A, 'shape') else (len(A[0]) if A else 0)

def shape(A):
    return rows(A), cols(A)

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, fn):
    """
    returns a num_rows x num_cols matrix
    whose (i,j)th entry is fn(i, j)
    """
    return [[fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

def identity(n):
    return make_matrix(n, n, is_diagonal)

def matrix_multiply(A, B):
    if cols(A) != rows(B):
        raise RuntimeError("Can't multiply matrices with dimensions {} and {}".format(
            shape(A), shape(B)))

    return [[dot(row,col) for col in zip(*B)] for row in A]

