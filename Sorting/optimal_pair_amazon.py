#find optimal pair which uses max memory utilization

def optimal_pair(capacity, fore, back):
    output = []
    i, j = 0, len(back) - 1
    cur_min_diff = 0

    while (i < len(fore) and j >= 0):
        pair_sum = fore[i][1] + back[j][1]

        if pair_sum <= capacity:
            if capacity - pair_sum == cur_min_diff:
                output.append([fore[i][0],back[j][0]])
            else:
                output = [[fore[i][0],back[j][0]]]
                cur_min_diff = capacity - pair_sum
            i += 1
        else:
            j -= 1
    return output
    
capacity = 10
foregroundList = [[1, 3],[2, 5],[3, 7],[4, 10]]
backgroundList = [[1, 2],[2, 3],[3, 4],[4, 5]]
print(optimal_pair(capacity, foregroundList, backgroundList))
