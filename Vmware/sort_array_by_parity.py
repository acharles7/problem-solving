"""
Given an array A of non-negative integers, return an array consisting 
of all the even elements of A, followed by all the odd elements of A.
"""

def sortArrayByParity(A):
    ptr, i = 0, 0
    while i < len(A):
        if A[i] % 2 == 0:
            A[ptr], A[i] = A[i], A[ptr]
            ptr += 1
        i += 1
    return A
A = [1,6,8,3,0,2,3,4,5,6,7,9]
print(sortArrayByParity(A))
