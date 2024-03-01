# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return
        
        def construct(left, right):
            
            if left > right:
                return
            
            curMax = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[curMax]:
                    curMax = i
            
            root = TreeNode(nums[curMax])
            
            root.left = construct(left, curMax - 1)
            root.right = construct(curMax + 1, right)
            
            return root
        
        return construct(0, len(nums) - 1)
        
        
            
        