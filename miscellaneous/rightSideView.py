"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
""" 

from collections import deque

def rightSideView(root: TreeNode) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    output = [root.val]

    while queue:
        last = queue.popleft()
        level = []
        
        for node in last:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)

        if level:
            output.append(level[-1].val)
            stack.append(level)
    return output
      

