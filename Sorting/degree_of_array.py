

from collections import Counter

def findShortestSubArray(A):
    left, right, count = {}, {}, {}
    for i, x in enumerate(A):
        if(x not in left):
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1

    ans = len(A)
    degree = max(count.values())

    for x in count:
        if(count[x] == degree):
            ans = min(ans, right[x] - left[x] + 1)
    return ans

A = [2, 5, 1, 2, 1, 2, 3, 1]
print(findShortestSubArray(A))
