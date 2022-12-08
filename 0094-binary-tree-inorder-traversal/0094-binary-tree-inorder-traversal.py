# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def inorder(root):
            
            if not root:
                return ""
            # if root and root.left:
            #     return inorder(root.left)
            # if root and root.right:
            #     return inorder(root.right)
            return inorder(root.left)+" "+str(root.val)+" "+inorder(root.right)+" "
       
        return   map(int,inorder(root).split())