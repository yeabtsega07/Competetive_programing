# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        
        def inorder( root ):
            
            if not root:
                return
            
            nodes.append(inorder(root.left))
            nodes.append(root.val)
            nodes.append(inorder(root.right))
        
        inorder( root )
        result = []
        for node in nodes:
            if not (node == None):
                result.append(node)
        result.sort()

        return result[k - 1]