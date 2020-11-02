
def get_mappings(self, board):
    mapping = {}
    is_reverse = True
    cell = 1

    for i in range(len(board)-1, -1, -1):
        if is_reverse:
            for j in range(len(board[0])):
                mapping[cell] = (i,j)
                cell += 1
            is_reverse = False
        else:
            for j in range(len(board[0])-1, -1, -1):
                mapping[cell] = (i,j)
                cell += 1
            is_reverse = True
    return mapping
def snakesAndLadders(self, board: List[List[int]]) -> int:
    n = len(board)

    mapping = self.get_mappings(board)

    first, last = 1, len(board)*len(board[0])
    queue = [1]
    distance = {1:0}

    while queue:
        cell = queue.pop(0)

        if cell == n*n:
            return distance[cell]

        for new_cell in range(cell+1, min(cell+6, n*n)+1):
            row, col = mapping[new_cell]

            if board[row][col] != -1:
                new_cell = board[row][col]

            if new_cell not in distance:
                distance[new_cell] = distance[cell] + 1
                queue.append(new_cell)
    return -1


