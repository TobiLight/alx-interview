#!/usr/bin/python3
# File: 0-nqueens.py
# Author: Oluwatobiloba Light
"""
N Queens Puzzle
"""
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
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


def solve_nqueens_util(board, row, N):
    solutions = []
    # Base case: if all queens are placed, print the solution
    if row == N:
        print(row)
        for i in range(len(board)):
            if 1 in board[i]:
                solutions.append([i, board[i].index(1)])
        # return solutions

    if len(solutions) == N:
        return solutions

    # Try placing queen in each column of this row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place queen in this position
            board[row][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(board, row + 1, N)

            # Backtrack
            board[row][col] = 0


def nqueens(N: int):
    """Solves the N queens problem"""
    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty N×N board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N Queens problem
    print("soll", solve_nqueens_util(board, 0, N))


if __name__ == "__main__":
    # if called with the wrong number of arguments
    if len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    # check if N is an integer
    try:
        N = int(N)
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    nqueens(N)
