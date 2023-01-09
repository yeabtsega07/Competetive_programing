# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            
            if not root:
                return ""
            return str(root.val)+" "+preorder(root.left)+" "+preorder(root.right)+" "
       
        return   map(int,preorder(root).split())