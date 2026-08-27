
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def count_nodes(root: TreeNode) -> int:
    # Base Case: If the current node is empty, it contributes 0 to the count
    if root is None:
        return 0
    
    # Recursive Step: Count 1 (current node) + all nodes on the left + all nodes on the right
    return 1 + count_nodes(root.left) + count_nodes(root.right)

