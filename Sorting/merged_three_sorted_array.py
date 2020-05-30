# Merged three sorted array
def merged(A, B):
    X = []
    m = len(A)
    n = len(B)
    i = 0
    j = 0
    while i < m and j < n:
        if A[i] <= B[j]:
            X.append(A[i])
            i += 1
        else:
            X.append(B[j])
            j += 1
    while i < m:
        X.append(A[i])
        i += 1
    while j < n:
        X.append(B[j])
        j += 1
    return X


A = [4, 7, 9, 11, 21]
B = [5, 7, 9, 14, 18]
C = [1, 100, 190, 500]

T = merged(A, B)
out = merged(T, C)
print(out)
