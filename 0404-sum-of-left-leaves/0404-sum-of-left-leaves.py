# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def solve(node, isLeft):
            
            if not node:
                return 0
            
            if node.left == None and node.right == None and isLeft:
                return node.val
            
            return solve(node.left, True) + solve(node.right, False)
        
        return solve(root, False)