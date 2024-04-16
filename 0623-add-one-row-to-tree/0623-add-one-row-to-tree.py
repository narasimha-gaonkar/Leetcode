# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def find_depth(node, height):
            if not node:
                return root

            left = find_depth(node.left, height + 1)
            right = find_depth(node.right, height + 1)
            
            if height == depth - 1:
                node.left = TreeNode(val, left = node.left)
                
                node.right = TreeNode(val, right = node.right)

        if depth == 1:
            node = TreeNode(val, left=root)
            return node

        find_depth(root, 1)
        return root
            
            
            
        