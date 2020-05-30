# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.


def moveZeroes(A):
    non_zero = 0
    for i in range(len(A)):
        if A[i] != 0:
            A[non_zero] = A[i]
            non_zero += 1
    for j in range(non_zero, len(A)):
        A[j] = 0
    return A


A = [0, 1, 0, 3, 12]
print(moveZeroes(A))
