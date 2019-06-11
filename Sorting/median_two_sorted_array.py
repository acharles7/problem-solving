#median of two sorted array
#Time Complexity: O(n)

def merge_two_array(A, B):
    X = []
    m, n = len(A), len(B)
    i, j = 0, 0
    while(i < m and j < n):
        if(A[i] <= B[j]):
            X.append(A[i])
            i += 1
        else:
            X.append(B[j])
            j += 1
    while(i < m):
        X.append(A[i])
        i += 1
    while(j < n):
        X.append(B[j])
        j += 1

    return X

def median(M):
    mid = len(M) // 2
    if(len(M) % 2 != 0):
        return M[mid]
    else:
        return (M[mid] + M[mid-1]) / 2

A = [-4, -1, 0, 4, 7, 11, 30]
B = [-8, 0, 1, 30, 32, 40]
C = merge_two_array(A, B)
print("Median: ",median(C))
