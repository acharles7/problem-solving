# LeetCode's Squares of a Sorted Array
# Given an array of integers A sorted in non-decreasing order, return
# an array of the squares of each number, also in sorted non-decreasing order.


# Time Complexity: O(n)
# Space Complexity: O(n)


def sortedSquares_n(A):
    n = len(A)
    i, j = 0, 0
    while j < n and A[j] < 0:
        j += 1
    i = j - 1
    res = []
    while 0 <= i and j < n:
        if A[i] ** 2 < A[j] ** 2:
            res.append(A[i] ** 2)
            i -= 1
        else:
            res.append(A[j] ** 2)
            j += 1

    while 0 <= i:
        res.append(A[i] ** 2)
        i -= 1
    while j < n:
        res.append(A[j] ** 2)
        j += 1
    return res


# Time Complexity: O(nlogn)
# Space Complexity: O(n)


def sortedSquares(A):
    X = []
    for i in A:
        square = i * i
        X.append(square)
    return sorted(X)


def sortedSquares_one_liner(A):
    return sorted(i * i for i in A)


A = [-4, -1, 0, 3, 10]
print(sortedSquares(A))
print(sortedSquares_one_liner(A))
print(sortedSquares_n(A))
