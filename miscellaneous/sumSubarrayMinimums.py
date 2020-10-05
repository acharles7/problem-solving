"""
Given an array of integers A, find the sum of min(B), 
where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.
"""


def sumSubarrayMins(A):
    minimum = 0
    for k in range(1, len(A)+1):
        for i in range(len(A)-k+1):
            minimum += min(A[i:i+k])
    return minimum


def sumSubarrayMins2(A):
    N = len(A)
    stack, left, right = [], [None]*N,  [None]*N

    for i in range(N):
        while stack and A[i] <= A[stack[-1]]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    for i in range(N-1, -1, -1):
        while stack and A[i] < A[stack[-1]]:
            stack.pop()
        right[i] = stack[-1] if stack else N
        stack.append(i)


    count = sum((i-left[i])* (right[i]-i)*A[i] for i in range(N))
    return count % (10**9 + 7)
        

A = [3, 1, 2, 4]
sumSubarrayMins2(A) 

