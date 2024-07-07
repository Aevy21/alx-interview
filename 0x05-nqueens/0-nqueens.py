#!/usr/bin/python3
""" This script solves the N queens puzzle, which involves placing N non-attacking queens on an N×N chessboard. """


import sys


def is_safe(board, row, col, N):
    """Check if a queen can be placed on board at (row, col) without being attacked."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N, solutions):
    """Use backtracking to find all solutions for the N queens problem."""
    if col >= N:
        solutions.append([[r, board[r].index(1)] for r in range(N)])
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N, solutions) or res
            board[i][col] = 0  # Backtrack

    return res

def nqueens(N):
    """Initialize the board and solve the N queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
