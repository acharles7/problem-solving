# LeetCode's Duplicate Zeros
# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.

def duplicateZeros(A):
    n = len(A)
    i = 1
    while(i <= n):
        if(A[i - 1] == 0):
            A.insert(i, 0)
            A.pop(-1)
            i += 2
        else:
            i += 1
    return A

A = [1,0,2,3,0,4,5,0]
print(duplicateZeros(A))
