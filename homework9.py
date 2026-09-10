class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def print_even_inorder(root):
    if root is None:
        return
    
    print_even_inorder(root.left)
    if root.data % 2 == 0:
        print(root.data, end=" ")
    print_even_inorder(root.right)


if __name__ == "__main__":

    values = [6, 2, 8, 1, 4, 7, 9, 3, 5, 10]
    root = None
    
    for val in values:
        root = insert(root, val)
        
    print("Even numbers in sorted order:")
    print_even_inorder(root)
    print()  

