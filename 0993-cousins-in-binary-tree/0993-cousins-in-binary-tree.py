# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    
        
        def solve(node, x_y_value, parent, depth):
            
            if not node:
                return None, None
            
            if node.val == x_y_value:
                return parent, depth
            
            l_parent, l_depth = solve(node.left, x_y_value, node, 1 + depth)
            
            r_parent, r_depth = solve(node.right, x_y_value, node, 1 + depth)
            
            return l_parent or r_parent, l_depth or  r_depth
        
        x_parent, x_depth = solve(root, x, None, 0)
        
        y_parent, y_depth = solve(root, y, None, 0)
        
        # print(x_parent, x_depth, y_parent, y_depth )
        return x_depth == y_depth and x_parent != y_parent