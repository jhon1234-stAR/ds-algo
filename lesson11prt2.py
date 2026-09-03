class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_min(root):
   
    if root is None:
        return None
    
 
    current = root
    while current.left is not None:
        current = current.left
        
    return current.data

# --- Example Usage 
if __name__ == "__main__":
  
    root = TreeNode(0)
    root.left = TreeNode(115)
    root.right = TreeNode(1534)
    root.left.left = TreeNode(-111)## change to smallest number plz

  
    min_value = find_min(root)
    print(f"Output: {min_value}")  # 

