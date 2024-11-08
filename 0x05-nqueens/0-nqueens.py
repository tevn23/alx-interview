#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the given row and column.

    Args:
        board (list): Current state of the board with queen positions.
        row (int): Row index for the queen to be placed.
        col (int): Column index for the queen to be placed.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        N (int): Size of the board (N x N) and number of queens to place.
    """
    def place_queens(board, row):
        """
        Recursively place queens on the board and print solutions.

        Args:
            board (list): Current state of the board with queen positions.
            row (int): Current row to attempt to place a queen.
        """
        if row == N:
            print_solution(board)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(board, row + 1)

    def print_solution(board):
        """
        Print a single solution in the required format.

        Args:
            board (list): Finalized board configuration with queen positions.
        """
        print([[i, board[i]] for i in range(N)])

    board = [-1] * N
    place_queens(board, 0)


def main():
    """
    Parse command-line arguments and initiate the N-Queens solver.

    Validates the input to ensure the correct number of arguments, that N is
    an integer, and that N is at least 4. Prints error messages and exits if
    the input is invalid.
    """
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

    solve_nqueens(N)


if __name__ == "__main__":
    main()
