# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        result = [0]
        
        def traverse( node ):
            
            if not node:
                return 0, 0
            
            left_count, left_sum = traverse(node.left)
            right_count, right_sum = traverse(node.right)
            
            cur_sum = left_sum + right_sum + node.val
            cur_count = left_count + right_count + 1
            cur_average = cur_sum // cur_count
            
            if node.val == cur_average:
                result[0] += 1
            
            return cur_count, cur_sum
        
        traverse( root )
        
        return result[0]