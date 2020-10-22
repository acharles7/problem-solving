"""
Given the root of a binary tree, find the maximum average value of any subtree of that tree.
1120. Maximum Average Subtree
"""

def maximumAverageSubtree(root: TreeNode) -> float:
    if not root: return 0

    def traverse_subtree(node):
        if node:
            container.append(node.val)
            traverse_subtree(node.left)
            traverse_subtree(node.right)

    container = []
    max_average = 0
    stack = [root]

    while stack:
        node = stack.pop(0)
        traverse_subtree(node)
        max_average = max(max_average, sum(container)/len(container))
        container.clear()

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return max_average

@dataclasses.dataclass  
class Node: 
    val:int
    count:int
    average:float
        
def helper(self, root):
    if not root: 
        return Node(0, 0, 0)

    left  = self.helper(root.left)
    right = self.helper(root.right)

    node_count = left.count + right.count + 1
    node_sum = left.val + right.val + root.val

    node_average = max([node_sum/node_count, left.average, right.average])

    return Node(node_sum, node_count, node_average)
        
def maximumAverageSubtree(root: TreeNode) -> float:
    return self.helper(root).average


