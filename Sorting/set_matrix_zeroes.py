# Given a m x n matrix, if an element is 0, set its entire row and column to 0. 

def setZeroes(matrix):
    row = set()
    col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row:
                matrix[i][j] = 0
            if j in col:
                matrix[i][j] = 0
    print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
