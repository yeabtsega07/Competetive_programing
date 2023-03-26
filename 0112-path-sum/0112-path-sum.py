# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse ( root, cur_sum = 0 ):
            
            if  not root:
                return False
            
            cur_sum += root.val
            
            if not root.left and not root.right and cur_sum == targetSum:
                
                return True
            
            return traverse( root.left, cur_sum ) or traverse( root.right, cur_sum )
        
        return traverse( root )
        