# LeetCode's Path Sum

# Given a binary tree and a sum, determine if the tree has a root-to-leaf
# path such that adding up all the values along the path equals the given sum.

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum(root, sum):
    if not root:
        return False

    path = [(root, sum - root.val)]
    while path:
        node, curr_sum = path.pop()

        if not node.left and not node.right and curr_sum == 0:
            return True
        if(node.left):
            path.append((node.left, curr_sum - node.left.val))
        if(node.right):
            path.append((node.right, curr_sum - node.right.val))
    return False

if(__name__ == "__main__"):
    sum = 9
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(10)
    root.left.left.right = Node(11)
    root.right.right.left = Node(8)

    print(hasPathSum(root, sum))
