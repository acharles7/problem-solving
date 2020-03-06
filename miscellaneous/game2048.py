def printGrid(mat):
    for row in mat:
        print(row)
    print()

def move_left(col):
    new_col = [0]*len(col)
    j = 0
    previous = None
    for i in range(len(col)):
        if col[i] != 0:
            if previous == None:
                previous = col[i]
            else:
                if previous == col[i]:
                    new_col[j] = 2 * col[i]
                    j += 1
                    previous = None
                else:
                    new_col[j] = previous
                    j += 1
                    previous = col[i]
    if previous != None:
        new_col[j] = previous
    return new_col

def game2048(grid, path):
    for swipe in path:
        if swipe == 'R':
            for i in range(len(grid)):
                grid[i] = move_left(grid[i][::-1])[::-1]

            printGrid(grid)
        elif swipe == 'L':
            for i in range(len(grid)):
                grid[i] = move_left(grid[i])
            printGrid(grid)
        elif swipe == 'U':
            temp_grid = []
            for i in range(len(grid)):
                col = []
                for j in range(len(grid[0])):
                    col.append(grid[j][i])
                swiped = move_left(col)
                for j in range(4):
                    grid[j][i] = swiped[j]
            printGrid(grid)
        elif swipe == 'D':
            temp_grid = []
            for i in range(len(grid)):
                col = []
                for j in range(len(grid[0])):
                    col.append(grid[j][i])
                swiped = move_left(col[::-1])[::-1]
                for j in range(4):
                    grid[j][i] = swiped[j]
            printGrid(grid)
    return grid

grid = [[0,2,0,2],
        [0,4,4,2],
        [0,0,4,2],
        [0,0,4,2]]
path = 'RRUD'
game2048(grid, path)
