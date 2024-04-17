# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def solve(node):
            nonlocal max_sum
            if not node:
                return 0
            
            lsum = max(0, solve(node.left))
            rsum = max(0, solve(node.right))
            max_sum = max(max_sum, lsum + rsum + node.val)
            return node.val + max(lsum, rsum)
            
        solve(root)
        return max_sum