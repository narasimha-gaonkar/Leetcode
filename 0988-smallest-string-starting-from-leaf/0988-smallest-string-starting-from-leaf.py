# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
            min_str = ''
            def solve(node, path):
                nonlocal min_str
                if not node:
                    return ''
                
                path = str(chr(97 + node.val)) + path
                
                if node.left == None and node.right == None:
                    if min_str == '':
                        min_str = path
                    else:
                        min_str = min(path, min_str)
                    # print(min_str)
                    return min_str
                
                l = solve(node.left, path)
                r = solve(node.right, path)
                
                return min(l ,r)
            
            solve(root, '')
            return min_str
                
                