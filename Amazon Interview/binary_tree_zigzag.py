
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return root
    queue = [[root]]
    while(len(queue[-1]) > 0):
        level = []
        for node in queue[-1]:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        queue.append(level)
    queue.pop()

    output = []
    left = True
    for level in queue:
        level_order = []
        if left:
            for node in level:
                level_order.append(node.val)
            left = False
        else:
            for node in reversed(level):
                level_order.append(node.val)
            left = True
        output.append(level_order)
    return output
