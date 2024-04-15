# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def solve(node, cur_sum):
            if not node:
                return 0
            cur_sum = cur_sum * 10 + node.val
            if node.left == None and node.right == None:
                return cur_sum
        
            cur_sum = solve(node.left, cur_sum) + solve(node.right, cur_sum)
            return cur_sum
        
        return solve(root, 0)
        
            
        