class Solution:
    def __init__(self):
        self.count = 0

    def isAttacked(self, board, row, col):
        column = [board[i][col] for i in range(len(board))]
        if column.count('Q') > 0:
            return True

        diag1 = [board[row-i][col-i] for i in range(1, min(row, col)+1)]
        diag2 = [board[row-i][col+i] for i in range(1, min(row, len(board[row])-col-1)+1)]

        if diag1.count('Q') > 0 or diag2.count('Q') > 0:
            return True
        return False

    def solveHelper(self, board, row):
        for j in range(len(board)):
            if not self.isAttacked(board, row, j):
                board[row][j] = 'Q'
                self.solveHelper(board, row + 1)
                board[row][j] = '.'

        if ''.join([''.join(r) for r in board]).count('Q') == len(board):
            self.count += 1

    def solveNQueens(self, n):
        board = [['.']*n for _ in range(n)]
        self.solveHelper(board, 0)
        return self.count
        
nqueen = Solution()
nqueen.solveNQueens(4)
print(nqueen.count)

