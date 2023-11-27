#!/usr/bin/python3
import sys
"""queens problem solved"""


def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, row, n, solutions):

    if row == n:
        solutions.append(board_to_result(board, n))
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0


def board_to_result(board, n):

    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                result.append([i, j])
                break
    return result


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    for sol in solutions:
        print(sol)
