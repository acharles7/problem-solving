'''
Given a binary tree, return the values of its boundary in anti-clockwise
direction starting from root. Boundary includes left boundary, leaves, and
right boundary in order without duplicate nodes.
(The values of the nodes may still be duplicates.)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    def getLeft(node):
        while node and (node.left or node.right):
            out.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

    def getRight(node):
        while node and (node.left or node.right):
            right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

    def getBottom(node):
        stack = [node]
        while stack:
            last = stack.pop()
            if last and not last.left and not last.right:
                out.append(last.val)
            if last.right: stack.append(last.right)
            if last.left: stack.append(last.left)

    out, right = [], []

    if root.left or root.right: out.append(root.val)
    if root.left: getLeft(root.left)
    if root.right: getRight(root.right)
    if root: getBottom(root)

    return out+right[::-1]
