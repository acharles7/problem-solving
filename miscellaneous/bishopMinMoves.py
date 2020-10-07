"""
Given a bishop on a 8*8 chessboard, find minimum number of moves required to
reach from a given starting point and end point
"""

def printt(board):
    for row in board:
        print(row)
    print()
    
    
def is_possible(start, end):
    a, b = start
    p, q = end
    
    row1 = [0 if i % 2 == 0 else 1 for i in range(8)]
    row2 = [1 if i % 2 == 0 else 0 for i in range(8)]
    
    board = [row1 if i % 2 == 0 else row2 for i in range(8)]
    return board[a][b] == board[p][q]
         

def find_min_moves(start, end):
    
    if not is_possible(start, end):
        return f"Not Possible: Can not reach to destination({end}) with starting point ({start})"
    
    board = [[-1 for _ in range(8)] for _ in range(8)]
    
    i, j = start
    p, q = end

    board[p][q] = 0
    distance = 1
    points = [[p, q]]
    
    while points:
        temp = []
        for point in points:
            x, y = point
            if x+1 < 8 and y+1 < 8 and board[x+1][y+1] == -1:
                board[x+1][y+1] = distance
                temp.append([x+1, y+1])

            if x+1 < 8 and y-1 >= 0 and board[x+1][y-1] == -1:
                board[x+1][y-1] = distance
                temp.append([x+1, y-1])

            if x-1 >= 0 and y-1 >= 0 and board[x-1][y-1] == -1:
                board[x-1][y-1] = distance
                temp.append([x-1, y-1])

            if x-1 >= 0 and y+1 < 8 and board[x-1][y+1] == -1:
                board[x-1][y+1] = distance
                temp.append([x-1, y+1])
            
        distance += 1
        points = temp
        
    printt(board)
    
    curr_distance = board[i][j]
    path = []
    
    while i != p or j != q:
        if i+1 < 8 and j+1 < 8 and board[i+1][j+1] < curr_distance:
            curr_distance = board[i+1][j+1]
            path.append([i+1,j+1])
            i += 1
            j += 1
            
        if i+1 < 8 and j-1 >= 0 and board[i+1][j-1] < curr_distance:
            curr_distance = board[i+1][j-1]
            path.append([i+1,j-1])
            i += 1
            j -= 1
        
        if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] < curr_distance:
            curr_distance = board[i-1][j-1]
            path.append([i-1,j-1])
            i -= 1
            j -= 1
            
        if i-1 >= 0 and j+1 < 8 and board[i-1][j+1] < curr_distance:
            curr_distance = board[i-1][j+1]
            path.append([i-1,j+1])
            i -= 1
            j += 1
            
    return path
            
    
start = [2, 3]
end   = [3, 6]
find_min_moves(start, end)

