#Max Sliding Window using queue

import collections
import numpy as np
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

print(max_sliding_window(A, k))
