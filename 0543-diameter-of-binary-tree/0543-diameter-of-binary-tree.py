# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def solve(node):
            nonlocal res
            if not node:
                return 0
            
            lh = solve(node.left)
            rh = solve(node.right)
            
            res = max(res, lh + rh)
            
            return 1 + max(lh, rh)
        
        solve(root)
        return res
        