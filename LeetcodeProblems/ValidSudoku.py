# You are given a 9x9 sudoku board board. A sudoku board is valid if the following rules are followed:
    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Return true if the sudoku board is valid, otherwise return false.
# Time Complexlity: 0(n^2)
# Space Complexlity: 0(n^2)
# Note: A sudoku board does not need to be full or be solveable to be valid.
# Example 1:
    # Input: board =
    #[["1","2",".",".","3",".",".",".","."],
    # ["4",".",".","5",".",".",".",".","."],
    # [".","9","8",".",".",".",".",".","3"],
    # ["5",".",".",".","6",".",".",".","4"],
    # [".",".",".","8",".","3",".",".","5"],
    # ["7",".",".",".","2",".",".",".","6"],
    # [".",".",".",".",".",".","2",".","."],
    # [".",".",".","4","1","9",".",".","8"],
    # [".",".",".",".","8",".",".","7","9"]]

    # Output: true

import collections
from typing import List

class Soultion:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c]:
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
