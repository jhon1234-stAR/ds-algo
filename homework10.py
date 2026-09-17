class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
  
    if root is None:
        return Node(key)
    
   
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

def minValueNode(node):
    current = node
  
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's key
    if key < root.val:
        root.left = delete(root.left, key)

    elif key > root.val:
        root.right = delete(root.right, key)
 
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        
        temp = minValueNode(root.right)



        root.val = temp.val

        root.right = delete(root.right, temp.val)

    return root

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(str(root.val))
        inorder(root.right, result)
    return result

def main():
    root = None
    
    while True:
        print("\n1. Insert Number")
        print("2. Delete Number")
        print("3. Show Tree (Inorder)")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            try:
                num = int(input("Enter number to insert: "))
                root = insert(root, num)
                print(f"Inserted {num}")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '2':
            try:
                num = int(input("Enter number to delete: "))
                root = delete(root, num)
                print(f"Deleted {num} (if it existed)")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '3':
            tree_elements = inorder(root)
            if tree_elements:
                print("Tree (Inorder): " + ", ".join(tree_elements))
            else:
                print("Tree is empty.")
                
        elif choice == '4':
            print("Exiting application.")
            break
        else:
            print("Invalid choice! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
