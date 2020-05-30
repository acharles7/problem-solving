# Given a sorted array A of unique numbers, find the K-th missing number
# starting from the leftmost number of the array.


def missingElement(A, k):
    missing = [0]
    for i in range(1, len(A)):
        missing.append(A[i] - A[i - 1] - 1 + missing[-1])
    for i in range(1, len(missing)):
        if missing[i - 1] < k <= missing[i]:
            return A[i - 1] + k - missing[i - 1]


A = [1, 4, 7, 9, 10, 15]
K = 4
print(missingElement(A, K))
