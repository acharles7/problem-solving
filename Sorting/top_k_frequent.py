# Given a non-empty array of integers, return the k most frequent elements.

from collections import Counter


def topKFrequent(nums, k):
    res = []
    counter = sorted(Counter(nums).items(), reverse=True, key=lambda p: p[1])
    for i in range(k):
        res.append(counter[i][0])
    return res


nums = [1, 1, 10, 10, 10, 2, 2, 3, 7, 3, 3, 6, 4, 3]
k = 3
print(topKFrequent(nums, k))
