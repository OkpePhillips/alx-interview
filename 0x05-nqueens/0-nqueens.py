#!/usr/bin/python3
"""
N queens problem solving module
"""

import sys


def is_safe(board, row, col, N):
    """
    Checking when to place the queen on the board
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N):
    """
    Solving the nqueens challenge
    """
    if row == N:
        print("[{}]".format(", ".join("[{}, {}]".format(i,
              board[i].index(1)) for i in range(N))))
        return True

    res = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            res = solve_nqueens(board, row + 1, N) or res
            board[row][col] = 0

    return res


def nqueens(N):
    """
    Recursively solving the problem
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    if not solve_nqueens(board, 0, N):
        print("No solution exists")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
