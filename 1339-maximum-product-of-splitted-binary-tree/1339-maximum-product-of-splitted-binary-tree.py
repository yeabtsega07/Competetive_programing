# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        temp = root
        def addT(temp):
            if not temp:
                return 0
            return temp.val + addT(temp.left) + addT(temp.right)
        # print(addT(temp), root)
        self.total = addT(temp)
        self.max_ = 0
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            self.max_ = max(self.max_, (self.total - left) * left, (self.total - right) * right)
            
            return left + right + root.val
            
            
            
        helper(root)
        return self.max_ % (pow(10 , 9) + 7)