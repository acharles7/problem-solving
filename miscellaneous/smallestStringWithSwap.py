"""
You are given a string s, and an array of pairs of indices in the string pairs 
where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.
"""

from collections import defaultdict
  
def smallestStringWithSwaps(s, pairs):
    
    graph = defaultdict(list)
    visited = [False]*len(s)
    out = [None]*len(s)
    
    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(i, stash):
        visited[i] = True
        stash.append(i)

        for vertice in graph[i]:
            if not visited[vertice]:
                stash = dfs(vertice, stash)
        return stash
    
    
    for i in range(len(s)):
        if not visited[i]:
            indices = sorted(dfs(i, []))
            letters = sorted([s[i] for i in indices])
            
            for indice, letter in zip(indices, letters):
                out[indice] = letter
    return ''.join(out)
    
s = "dcab"
pairs = [[0,3],[1,2], [0,2]]
smallestStringWithSwaps(s, pairs)

