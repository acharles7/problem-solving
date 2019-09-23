def searchMatrix(matrix, target):
    row = len(matrix) - 1
    col = 0
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    while col < len(matrix[0]) and row >= 0:
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix, target))
