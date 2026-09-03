class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_nodes(root):
   
    if root is None:
        return 0
    
   
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)


if __name__ == "__main__":
   
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    total_sum = sum_nodes(root)
    print(f"Output: {total_sum}")  

