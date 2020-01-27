'''
There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B,
and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.
'''

# DFS
def dfs(M, visited, i):
    for j in range(len(M)):
        if M[i][j] == 1 and visited[j] == 0:
            visited[i] = 1
            dfs(M, visited, j)


def findCircleNum(M) -> int:
    visited = [0]*len(M)
    count = 0

    for i in range(len(M)):
        if visited[i] == 0:
            dfs(M, visited, i)
            count += 1
    return count

#BFS

def findCircleNumBfs(M):
    visited = [0]*len(M)
    count = 0
    queue = []
    for i in range(len(M)):
        if visited[i] == 0:
            queue.append(i)
            while queue:
                last = queue.pop(0)
                visited[last] = 1

                for j in range(len(M)):
                    if M[last][j] == 1 and visited[j] == 0:
                        queue.append(j)
            count += 1
    return count

M = [[1,1,0],[1,1,1],[0,1,1]]
print(findCircleNumBfs(M))
