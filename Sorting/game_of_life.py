# LeetCode's Game of Life
# Write a function to compute the next state (after one update) of the board given its current state.

def gameOfLife(board):
    def getCount(copy_board,i, j):
        neighbours = [0] * 8
        count = 0

        neighbours[0] = copy_board[i][j-1]       #left_horizontal
        neighbours[1] = copy_board[i][j+1]       #right_horizontal
        neighbours[2] = copy_board[i-1][j]       #up_vertical
        neighbours[3] = copy_board[i+1][j]       #down_vertical
        neighbours[4] = copy_board[i-1][j-1]     #left_up_diagonal
        neighbours[5] = copy_board[i-1][j+1]     #right_up_diagonal
        neighbours[6] = copy_board[i+1][j-1]     #left_down_diagonal
        neighbours[7] = copy_board[i+1][j+1]     #right_down_diagonal

        for i in neighbours:
            if i == 1:
                count += 1
        return count

    def getAnswer(cell, count):
        if cell == 1:
            if count < 2:
                return 0
            elif count == 2 or count == 3:
                return 1
            elif count > 3:
                return 0
        else:
            if count == 3:
                return 1
            return 0
    def preprocessBoard(boardy):
        boardy.insert(0, [0]*len(boardy[0]))
        boardy.append([0]*len(boardy[0]))

        for row in boardy:
            row.insert(0, 0)
            row.append(0)
        return boardy

    new_board = [[board[row][col] for col in range(len(board[0]))] for row in range(len(board))]

    new_board = preprocessBoard(new_board)

    for i in range(1, len(new_board) - 1):
        for j in range(1, len(new_board[0]) - 1):
            count = getCount(new_board, i, j)
            answer = getAnswer(new_board[i][j], count)
            board[i-1][j-1] = answer
    return board


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board))
