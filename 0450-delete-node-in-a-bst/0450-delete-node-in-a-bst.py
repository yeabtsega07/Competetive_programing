# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # to find the inorder successor
        def get_min ( node ):
            current = node
            
            while current.left:
                current = current.left
            
            return current
        
        
        if not root:
            return 
        
        if root.val == key:
            
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            check = get_min( root.right )

            root.val = check.val
            root.right = self.deleteNode(root.right, check.val)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
            