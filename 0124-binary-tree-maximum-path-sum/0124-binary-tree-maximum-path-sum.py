# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.helper(root)
        return self.maxSum
    
    def helper(self, root):
        if not root: return 0
        leftSum = max(0, self.helper(root.left))
        rightSum = max(0, self.helper(root.right))

        self.maxSum = max(self.maxSum, leftSum + rightSum + root.val)

        return max(leftSum, rightSum) + root.val
        