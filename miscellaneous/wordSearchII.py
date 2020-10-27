"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
"""

from collections import defaultdict

def printt(grid):
    for row in grid:
        print(row)
    print()
    
    
def hasWord(grid, word, i, j, count):
    if count == len(word): return True
    
    if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] != word[count]:
        return False

    temp = grid[i][j]
    grid[i][j] = '*'
    
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    for dx, dy in directions:
        if hasWord(grid, word, i + dx, j + dy, count+1): 
            return True
    grid[i][j] = temp
    return False
    
    
def findWord(board, word, indexes):
    first = word[0]
    for i, j in indexes[first]:
        if hasWord([row[:] for row in board], word, i, j, 0):
            return True
    return False
    
def getIndexes(board):
    dic = defaultdict(list)
    for i in range(len(board)):
        for j in range(len(board[0])):  
            dic[board[i][j]].append((i, j))
    return dic


def findWords(board, words):
    printt(board)
    output = []
    indexes = getIndexes(board)
    for word in words: 
        if findWord(board, word, indexes):
            output.append(word)
    return output   
            
        
board = [['o','a','o','n'],
         ['e','t','n','e'],
         ['i','h','k','r'],
         ['i','f','l','v']]
words = ["zash", "oath", "pea","eat","rain", "neon", "kenn"]

print(findWords(board, words))

