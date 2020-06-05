def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return root

    if root.left and root.right:
        root.left, root.right = root.right, root.left
    elif root.left and not root.right:
        root.left, root.right = None, root.left
    elif not root.left and root.right:
        root.left, root.right = root.right, None

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
