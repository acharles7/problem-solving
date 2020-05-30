# Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which
# gives the sum of zero.


def three_sum(A):
    A.sort()
    res = []

    for i in range(len(A)):
        j, k = i + 1, len(A) - 1
        if i != 0 and A[i] == A[i - 1]:
            continue
        while j < k:
            if A[i] + A[j] + A[k] == 0:
                res.append([A[i], A[j], A[k]])
                j += 1
                while j < k and A[j] == A[j - 1]:
                    j += 1
            elif A[i] + A[j] + A[k] < 0:
                j += 1
            else:
                k -= 1
    return res


A = [-1, 0, 0, 1, 2, -1, -4]
print(three_sum(A))
