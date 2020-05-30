def mergeSorted(A, n, B, m):
    i = n - 1
    j = m - 1
    last = n + m - 1

    while j >= 0:
        if i > 0 and A[i] > B[j]:
            A[last] = A[i]
            i -= 1
        else:
            A[last] = B[j]
            j -= 1
        last -= 1


X = -1
A = [3, 5, 7, 9, 10, 13, 14, X, X, X, X]
B = [4, 6, 8, 15]
n = 7
m = 4

mergeSorted(A, n, B, m)
print("Sorted Array:", A)
