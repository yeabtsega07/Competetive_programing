# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        result = [float("inf")]
        
        def recur ( node, level ):
            
            if not node:
                return
            
            if not node.right and not node.left:
                result[0] = min(result[0], level)
                return
            
            recur(node.left, level + 1)
            recur(node.right, level + 1)
        
        recur(root, 1)
        
        return result[0] if result[0] != float("inf") else 0
        