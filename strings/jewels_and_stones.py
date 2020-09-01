def numJewelsInStones(J, S):
    count = {}
    cnt = 0
    for i in S:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in J:
        if i in count:
            cnt += count[i]
    return cnt

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J, S))
