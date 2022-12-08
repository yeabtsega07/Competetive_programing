# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def traverse(root):
                if root and  not root.left and not root.right:
                    return str(root.val)+" "
                if not root:
                    return ""
                return traverse(root.left) + traverse(root.right)
        # print(traverse(root1), traverse(root2) )     
        return traverse(root1) == traverse(root2)  
        