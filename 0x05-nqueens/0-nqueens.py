#!/usr/bin/python3
import sys

def print_usage_and_exit(message, status=1):
    print(message)
    sys.exit(status)

def is_safe(board, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    # Check if there's a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if i >= 0 and board[i] == j:
            return False
    # Check if there's a queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if i >= 0 and board[i] == j:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    if row == N:
        # A solution is found, format it as required and add to solutions
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(N, row + 1, board, solutions)
                board[row] = -1  # Reset the row

def nqueens(N):
    # Initial board setup
    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    
    if N < 4:
        print_usage_and_exit("N must be at least 4")

    nqueens(N)
