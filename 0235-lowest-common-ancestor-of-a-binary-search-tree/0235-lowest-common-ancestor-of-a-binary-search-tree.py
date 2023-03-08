# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        nodes = set()
        
        def pre_order ( root, p, last = None):
            
            if not root:
                return 
            
            if root not in nodes:
                nodes.add(root)
            else:    
                last = root
                
            if root.val > p.val:
                return pre_order(root.left, p, last)
            elif root.val < p.val:
                return pre_order(root.right, p, last)
            
            return last
        
        pre_order(root, p)
        return pre_order(root, q)
            
        
        