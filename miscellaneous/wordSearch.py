'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
'''

def search(board, i, j, idx, word):
    if idx == len(word):
        return True

    if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or board[i][j] != word[idx]:
        return False

    temp = board[i][j]
    board[i][j] = '*'

    if search(board, i-1, j, idx+1, word): return True
    if search(board, i+1, j, idx+1, word): return True
    if search(board, i, j-1, idx+1, word): return True
    if search(board, i, j+1, idx+1, word): return True

    board[i][j] = temp

    return False

def exist(board, word) -> bool:

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and search(board, i, j, 0, word):
                    return True
    return False

board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]

print(exist(board, "ABCCED"))
