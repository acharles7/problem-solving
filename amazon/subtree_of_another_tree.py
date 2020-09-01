# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def traverse(x):
        if x:
            return f"#{x.val}{traverse(x.right)}{traverse(x.left)}"
    return traverse(t) in traverse(s)
