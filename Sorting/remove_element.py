# Given an array nums and a value val, remove all instances of that
# value in-place and return the new length.

def removeElement(A, x):
    i = 0
    for j in range(len(A)):
        if(A[j] != x):
            A[i] = A[j]
            i += 1
    return i

def removeElement2(A, x):
    i = 0
    n = len(A)

    while(i < n):
        if(A[i] == x):
            A[i] = A[n - 1]
            n -= 1
        else:
            i += 1
    return n

A = [0,1,2,2,3,0,4,2]
x = 2
print(removeElement2(A, x))
