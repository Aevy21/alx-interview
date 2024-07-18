#!/usr/bin/python3
"""
Rotate an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (list of list of int): The matrix to rotate. Must be square.

    Returns:
    - None: The matrix is edited in-place.

    Raises:
    - ValueError: If the input matrix is not square.
    """

    n = len(matrix)

    if n != len(matrix[0]):
        raise ValueError("Input matrix must be square")

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
