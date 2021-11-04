class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

def preorder(root):
 
    # if root:
    #     print(root.val)
    #     preorder(root.left) 
    #     preorder(root.right)
    
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
 
    # if root:
    #     inorder(root.left)
    #     print(root.val)
    #     inorder(root.right)

    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
         

def postorder(root):
 
    # if root:
    #     postorder(root.left)
    #     postorder(root.right)
    #     print(root.val)
    
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(preorder(root))
print(inorder(root))
print(postorder(root))

