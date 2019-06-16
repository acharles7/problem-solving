#Search in a row wise and column wise sorted matrix

#Time Complexity: O(nˆ2)
def search(A, x):
    for row in range(len(A)):
        for col in range((len(A[row]))):
            if(A[row][col] == x):
                return [row,col]
    return 0

A = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
x = 37
print(search(A, x))
