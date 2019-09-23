
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

def copyRandomList(self, head: 'Node') -> 'Node':
    nodeDic = {}

    def getNode(node):
        if node:
            if node in nodeDic:
                return nodeDic[node]
            else:
                nodeDic[node] = Node(node.val,None,None)
                return nodeDic[node]
        return None

    if not head:
        return head

    oldNode = head
    newNode = Node(oldNode.val, None, None)
    nodeDic[oldNode] = newNode
    while oldNode != None:
        newNode.next = getNode(oldNode.next)
        newNode.random = getNode(oldNode.random)

        oldNode = oldNode.next
        newNode = newNode.next
    return nodeDic[head]
