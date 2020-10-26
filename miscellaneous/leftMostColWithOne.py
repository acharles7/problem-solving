# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

"""
Given a row-sorted binary matrix binaryMatrix, return leftmost 
column index(0-indexed) with at least a 1 in it. 
If such index doesn't exist, return -1.
"""

def left_most_column_with_one(binaryMatrix: 'BinaryMatrix') -> int:
    row, col = binaryMatrix.dimensions()
    r, c = 0, col-1

    while r < row and c >= 0:
        num = binaryMatrix.get(r, c)
        if num == 1:
            c -= 1
        else:
            r += 1

    if c+1 == col:
        return -1
    return c+1   

