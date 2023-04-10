# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def build( preorder, inorder ):
            
            if not preorder and not inorder:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = build( preorder[1 : mid + 1], inorder[: mid])
            root.right = build( preorder[mid + 1 : ], inorder[ mid + 1 : ])
            
            return root
        
        return build( preorder, sorted(preorder) )