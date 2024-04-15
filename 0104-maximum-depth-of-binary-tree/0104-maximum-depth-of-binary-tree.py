# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def solve(node):
            if not node:
                return 0
            res = max(1 + solve(node.left), 1 + solve(node.right))
            
            return res
        
        return solve(root)