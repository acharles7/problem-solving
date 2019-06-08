

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaves(root):
    s1 = []
    s2 = []

    s1.append(root)
    while(len(s1) != 0):
        current = s1.pop()

        if(current.left):
            s1.append(current.left)
        if(current.right):
            s1.append(current.right)
        elif(not current.left and not current.right):
            s2.append(current)

    for leaf in reversed(s2):
        print(leaf.data, end=' ')

if(__name__ == "__main__"):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(7)
    root.left.left.left = Node(10)
    root.left.left.right = Node(11)
    root.right.right.left = Node(8)

    print_leaves(root)
