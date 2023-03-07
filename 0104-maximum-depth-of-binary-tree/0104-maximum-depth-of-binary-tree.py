# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def inorder( node ):

            if not node:
                return 0
            
            left = right = 0
            left = inorder(node.left)
            right = inorder(node.right)
            
            return max(left, right) + 1


        return inorder( root )