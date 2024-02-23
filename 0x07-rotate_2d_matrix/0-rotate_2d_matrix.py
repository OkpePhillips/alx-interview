#!/usr/bin/python3
"""
Rotating a 2D matrix by 90 degrees
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transposing the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()
