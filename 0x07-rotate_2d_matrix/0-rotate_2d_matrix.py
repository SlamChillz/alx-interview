#!/usr/bin/python3
"""
2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return

    for i in range(rows // 2):
        for j in range(i, rows - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[rows - 1 - j][i]
            matrix[rows - 1 - j][i] = matrix[rows - 1 - i][rows - 1 - j]
            matrix[rows - 1 - i][rows - 1 - j] = matrix[j][rows - 1 - i]
            matrix[j][rows - 1 - i] = temp
