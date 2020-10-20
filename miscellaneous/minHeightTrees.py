"""
Leetcode 310. Minimum Height Trees
"""

from collections import defaultdict

def bfs_iterative(node, graph, visited):
    depth = 0
    queue = [[node]]

    while queue:
        last = queue.pop(0)
        level = []
        while last:
            n = last.pop()    
            visited.add(n)

            for ele in graph[n]:
                if ele not in visited:
                    level.append(ele)
        if level:
            depth += 1
            queue.append(level)         
    return depth

def find_min_height_trees(n, edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    heights = [bfs_iterative(i, graph, set()) for i in range(n)]
    return [i for i in range(n) if heights[i] == min(heights)]
        

assert find_min_height_trees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3, 4]
assert find_min_height_trees(4, [[1,0],[1,2],[1,3]]) == [1]
assert find_min_height_trees(2, [[0,1]]) == [0, 1]
assert find_min_height_trees(1, []) == [0]
find_min_height_trees(n, edges)

