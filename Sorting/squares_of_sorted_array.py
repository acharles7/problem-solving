def sortedSquares(A):
    X = []
    for i in A:
        square = i * i
        X.append(square)
    return(sorted(X))

A = [-4,-1,0,3,10]
print(sortedSquares(A))
