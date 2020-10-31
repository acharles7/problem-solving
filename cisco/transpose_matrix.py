"""
Given a matrix A, return the transpose of A.
"""


def transpose(self, A: List[List[int]]) -> List[List[int]]:        
    A_transpose = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            A_transpose[j][i] = A[i][j]
    return A
