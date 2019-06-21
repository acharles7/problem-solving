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


# Given a binary tree and a sum, find all root-to-leaf paths where
# each path's sum equals the given sum.


def pathSum(root, sum):
    paths = []
    cur_path = []

    def allPath(root, sum):
        if root is None:
            return False

        cur_path.append(root.val)
        sum -= root.val
        if(root.left == None and root.right == None and sum == 0):
            paths.append(list(cur_path))
        else:
            allPath(root.left, sum)
            allPath(root.right, sum)
        cur_path.pop()

    allPath(root, sum)
    return paths


if(__name__ == "__main__"):
    sum = 22
    root = Node(5)

    root.left = Node(4)
    root.right = Node(8)

    root.left.left = Node(11)

    root.right.left = Node(13)
    root.right.right = Node(4)

    root.left.left.left = Node(7)
    root.left.left.right = Node(2)

    root.right.right.left = Node(5)
    root.right.right.right = Node(1)

    print(hasPathSum(root, sum))
    print(pathSum(root, sum))
