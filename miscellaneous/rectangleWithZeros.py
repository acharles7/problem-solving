"""
Find all rectangles filled with 0.
Find the top left and bottom right coordinates of a rectangle of 0's within a matrix of 1's.
Expand it so it works for any number of rectangles

Reference: Karat Roblox
"""


def get_rectangle(grid, i, j, rect):
    """Get all coordinate of single rectangle"""
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1:
        return
    
    grid[i][j] = 1
    rect.append((i,j))
    
    get_zeros(grid, i-1, j, rect)
    get_zeros(grid, i, j+1, rect)
    get_zeros(grid, i, j-1, rect)
    get_zeros(grid, i+1, j, rect)
    return rect
    

def find_coordinates(grid):
    rectangles, coordinates = [], []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                rectangle = get_zeros(grid, i, j, [])
                rectangles.append(rectangle)
    
    for rectangle in rectangles:
        rectangle.sort(key=lambda x: (x[0], x[1]))
        coordinates.append([rectangle[0], rectangle[-1]])
        
    return coordinates
                
                
input1 = [[1, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 1, 1, 0]]

input2 = [[1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 1, 1],
          [1, 0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1]]

input3 = [[1, 0, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 1, 1, 1, 0]]

find_coordinates(input1)

