class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def left_view(root):
    if not root:
        return

    queue = [root]

    while len(queue):
        n = len(queue)
 
        for i in range(1, n + 1):
            node = queue[0]
            queue.pop(0)
 
            if (i == 1):
                print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

left_view(root)
