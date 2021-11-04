class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def inOrder(root):
     
    current = root
    stack = []
    done = 0
     
    while True:
        if current:
            stack.append(current)
            current = current.left
        
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        else:
            break

    print()

def iterativePreorder(root):
     
    if root is None:
        return
 
    nodeStack = []
    nodeStack.append(root)
 
    while(len(nodeStack) > 0):
         
        node = nodeStack.pop()
        print (node.data, end=" ")
         
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

# Post order
def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def postOrderIterative(root):
         
    # Check for empty tree
    if root is None:
        return
 
    stack = []
     
    while(True):
         
        while (root):
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
 
            root = root.left
         
        root = stack.pop()
 

        if (root.right is not None and
            peek(stack) == root.right):
            stack.pop()
            stack.append(root)
            root = root.right 
 
        else:
            ans.append(root.data)
            root = None
 
        if (len(stack) <= 0):
                break
 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
postOrderIterative(root)
