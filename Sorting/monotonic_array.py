# An array is monotonic if it is either monotone increasing or monotone decreasing.


def monotonic(A):
    increasing = True
    decreasing = True

    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            increasing = False
        if A[i] < A[i + 1]:
            decreasing = False
    return increasing or decreasing


A = [1, 2, 2, 3]
print(monotonic(A))
