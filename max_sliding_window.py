#Max Sliding Window using queue

import collections

def max_sliding_window(A, k):
    if not A:
        return A
    queue = collections.deque()
    res = []
    for n in  A:
        if(len(queue) < k):
            queue.append(n)
        else:
            res.append(max(queue))
            queue.popleft()
            queue.append(n)
    res.append(max(queue))
    return res

A = [1, 3, -1, -3, 5, 3, 6, 7]
k = 4
print(max_sliding_window(A, k))
