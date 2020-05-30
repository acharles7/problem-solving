# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied. Otherwise, it becomes vacant.

# Given the initial state of the prison, return the state of the prison after N days


def prisonAfterNDays(cells, N):
    def prisonAfterOneDay(cells):
        output = [0] * len(cells)
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                output[i] = 1
        return output

    output = []
    N = N % 14
    if N == 0:
        N = 14
    for i in range(N):
        output = prisonAfterOneDay(cells)
        cells = output
    return output


cells = [1, 0, 0, 1, 0, 0, 1, 0]
N = 10000000
print(prisonAfterNDays(cells, N))
