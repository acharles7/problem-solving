#Search in a row wise and column wise sorted matrix

#Time Complexity: O(nˆ2)
def search(A, x):
    for row in range(len(A)):
        for col in range((len(A[row]))):
            if(A[row][col] == x):
                return [row,col] #found
    return 0

#Time Complexity: O(n)
def search_in_n(A, x):
    i = 0
    j = len(A) - 1

    while(i < len(A) and j >= 0):
        if(A[i][j] == x):
            return [i,j] #found
        if(A[i][j] > x):
            j -= 1
        else:
            i += 1
    return 0

A = [[10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]]
x = 32
print(search(A, x))
print(search_in_n(A, x))
