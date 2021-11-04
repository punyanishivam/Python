class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLevelOrder(root):
    if not root:
        return

    queue = [root]

    while len(queue):
        print(queue[0].data)
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)
