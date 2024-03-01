# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        def solve(node):
            
            if node == None:
                return 0
            
            if node.val < low:
                return solve(node.right)
            elif node.val > high:
                return solve(node.left)
            return node.val + solve(node.left) + solve(node.right)
            
        return solve(root)