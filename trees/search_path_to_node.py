#Print path from root to all nodes in a Complete Binary Tree

def find_path_to_node(paths, root, N):
    if(root > N):
        return
    paths.append(root)

    for i in range(0,len(paths)):
        print(paths[i], end=' ')
    print()
    find_path_to_node(paths[:], root * 2, N)
    find_path_to_node(paths[:], root * 2 + 1, N)

N = 7
paths = []
find_path_to_node(paths, 1, N)
