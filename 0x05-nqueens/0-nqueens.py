#!/usr/bin/python3
"""
N-Queens Problem Solver
"""

import sys

def backtrack(row, n, occupied_cols, positive_diagonals, negative_diagonals, chessboard):
    """
    Backtracking function to find solutions for the N-Queens problem.
    """
    if row == n:
        solution = []
        for r in range(len(chessboard)):
            for c in range(len(chessboard[r])):
                if chessboard[r][c] == 1:
                    solution.append([r, c])
        print(solution)
        return

    for col in range(n):
        if col in occupied_cols or (row + col) in positive_diagonals or (row - col) in negative_diagonals:
            continue

        occupied_cols.add(col)
        positive_diagonals.add(row + col)
        negative_diagonals.add(row - col)
        chessboard[row][col] = 1

        backtrack(row + 1, n, occupied_cols, positive_diagonals, negative_diagonals, chessboard)

        occupied_cols.remove(col)
        positive_diagonals.remove(row + col)
        negative_diagonals.remove(row - col)
        chessboard[row][col] = 0

def solve_nqueens(n):
    """
    Solves the N-Queens problem and prints all possible solutions.
    Args:
        n (int): Number of queens. Must be >= 4.
    """
    occupied_cols = set()
    positive_diagonals = set()
    negative_diagonals = set()
    chessboard = [[0] * n for _ in range(n)]

    backtrack(0, n, occupied_cols, positive_diagonals, negative_diagonals, chessboard)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
