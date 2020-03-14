'''
In chess, queens can move any number of squares vertically, horizontally, or diagonally.
Find all the possible coordinates on an 8 × 8 chessboard that would be safe from the 
attack of a queen positioned at coordinate q.
Return the coordinates sorted in lexicographical order.
'''


def checkMark1(board, i, j):
    if i < 0 or i > 8 or j < 0 or j >= 8:
        return
    board[i][j] = '*'
    checkMark1(board, i-1, j+1)
    return board

def checkMark2(board, i, j):
    if i < 0 or i >= 8 or j < 0 or j >= 8:
        return
    board[i][j] = '*'
    checkMark2(board, i-1, j-1)
    return board

def checkMark3(board, i, j):
    if i < 0 or i >= 8 or j < 0 or j >= 8:
        return
    board[i][j] = '*'
    checkMark3(board, i+1, j+1)
    return board

def checkMark4(board, i, j):
    if i < 0 or i >= 8 or j < 0 or j >= 8:
        return
    board[i][j] = '*'
    checkMark4(board, i+1, j-1)
    return board


def chessQueen(q):
    mapping = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    board = [["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"],
             ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8"],
             ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"],
             ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8"],
             ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8"],
             ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8"],
             ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8"],
             ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]]

    row, col = mapping[q[0]], int(q[1])-1
    for i in range(8):
        board[row][i] = '*'
        
    for i in range(8):
        board[i][col] = '*'
        
    board = checkMark1(board, row, col)
    board = checkMark2(board, row, col)
    board = checkMark3(board, row, col)
    board = checkMark4(board, row, col)
    
    output = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != '*':
                output.append(board[i][j])
                
    return output  
chessQueen('b8')
