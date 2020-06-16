'''
Given a NxN Square Matrix, find the best campsite by having the closest in distance 
to all the POIs (Point of Interest) locations, while avoiding all the obstacles.

Returns the campsite location by coordinates in [x, y].

'*' :  Point of Interest
'X' :  Obstacle
'C' :  Possible campsite with the shortest distance to all the POIs
For example, C denotes the camp site location. Return that location's coordinates.

+-----------------------+
| * | X |   | * |   | * |
|   | X |   |   |   |   |
|   | X |   |   |   |   |
|   |   |   | C |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   | * |
+-----------------------+

'''


from copy import deepcopy

def bfs(grid, start):
    queue = [[start]]
    visited = set(start)
    distances = []
    while queue:
        path = queue.pop(0)
        x, y = path[-1]
        if grid[x][y] == '*':
            grid[x][y] = ' '
            distances.append(len(path))

        for x2, y2 in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] != 'X' and (x2, y2) not in visited:
                queue.append(path + [(x2, y2)])
                visited.add((x2, y2))
    return distances
    
def find_campsite(field):
    campsites = {}
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == 'C':
                distances = bfs(deepcopy(field), (i, j))
                campsites[(i, j)] = sum(distances)
    return campsites
    

field = [['*', 'X', ' ', '*', 'X', '*'],
         [' ', 'X', 'C', ' ', ' ', ' '],
         [' ', 'X', ' ', 'C', ' ', 'X'],
         ['C', ' ', ' ', ' ', ' ', ' '],
         [' ', 'X', 'X', ' ', 'X', '*'],
         [' ', 'X', '*', ' ', 'X', 'C']]
print(find_campsite(field))
