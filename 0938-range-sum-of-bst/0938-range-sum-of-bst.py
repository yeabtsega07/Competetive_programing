# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        if not root:
            return sum_
        
        if low <= root.val <= high: 
            sum_ += root.val
        
        sum_ += self.rangeSumBST(root.left, low, high)
        sum_  += self.rangeSumBST(root.right, low, high)
        
        # print(sum1, sum2)
        return sum_
        
        