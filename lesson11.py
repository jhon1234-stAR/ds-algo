class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

#example usage
root = Node(8)
insert(root, 3)
insert(root, 10)
insert(root, 10)
insert(root, 1)
insert(root, 6)
insert(root, 4)
insert(root, 7)
insert(root, 5)




def search(root,key):

    if root is None or root.val == key:
        return root
    
    if key < root.val:
        return search(root.left, key)

    return search(root.right, key)

#example usage 

found_Node = search(root,55
                    )

if found_Node:
    print("element found" , found_Node.val)

else:
    print("element not found")