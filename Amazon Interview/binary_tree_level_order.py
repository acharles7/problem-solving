def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return root

    output = []
    queue = [[root]]
    while(len(queue[-1]) > 0):
        level = []
        for r in queue[-1]:
            if r.left:
                level.append(r.left)
            if r.right:
                level.append(r.right)
        queue.append(level)
    queue.pop()

    for level in queue:
        level_node = []
        for node in level:
            level_node.append(node.val)
        output.append(level_node)
    return output
    
