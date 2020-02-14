'''
Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
'''

def verticalOrder(root):
    if not root:return []
    queue = [(root,0)]
    hashmap = defaultdict(list)
    while queue:
        node, idx = queue.pop(0)
        hashmap[idx] += [node.val]
        if node.left:
            queue.append((node.left, idx-1))
        if node.right:
            queue.append((node.right, idx+1))
    output = [hashmap[i] for i in sorted(hashmap)]
    return output
