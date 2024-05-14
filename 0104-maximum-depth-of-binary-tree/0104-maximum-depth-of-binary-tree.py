# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def solve(node):
            
            if node.left == None and node.right == None:
                return 1
            left = right = 0
            if node.left:
                left = 1 + solve(node.left) 
            if node.right:
                right = 1 + solve(node.right)
            
            return max(left, right)
        
        return solve(root)