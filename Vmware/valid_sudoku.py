from typing import List

"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be 
validated according to the following rules:

 1. Each row must contain the digits 1-9 without repetition.
 2. Each column must contain the digits 1-9 without repetition.
 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 
    without repetition.
"""

def is_valid_row(row):
    numbers = set()
    for num in row:
        if num != '.' and num in numbers:
            return  False
        numbers.add(num)
    return True

def get_grid(grid, start, end):
    return [grid[i][j] for i in range(len(grid)) for j in range(start, end)]
    
def isValidSudoku(board: List[List[str]]) -> bool:
    for row in board:
        if not is_valid_row(row):
            return False

    for row in zip(*board):
        if not is_valid_row(row):
            return False
    
    ranges = [(0, 3), (3, 6), (6, 9)]
    for start, end in ranges:
        for c_start, c_end in ranges:
            if not is_valid_row(get_grid(board[start:end], c_start, c_end)):
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))        
