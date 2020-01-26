def diameterOfBinaryTree(root):
    self.count = 0
    def depth(node):
        if not node: return 0
        L = depth(node.left)
        R = depth(node.right)
        self.count = max(self.count, L+R)
        return max(L, R) + 1
    depth(root)
    return self.count
