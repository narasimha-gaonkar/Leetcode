# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        view = {}
        
        def solve(node, level):
            
            if not node:
                return
            
            if level not in view:
                view[level] = node.val
            
            solve(node.right, 1 + level)
            solve(node.left, 1 + level)
            
            return 
        solve(root, 0)
        return view.values()
        