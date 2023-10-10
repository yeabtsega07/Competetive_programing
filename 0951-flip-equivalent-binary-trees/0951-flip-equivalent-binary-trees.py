# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if (not root1 and root2) or (not root2 and root1) :
            return False
        
        track = defaultdict(set)
        
        def get_childrens(node):
            
            if not node:
                return 
            
            if node.left:
                track[node.val].add(node.left.val)
                get_childrens(node.left)
            
            if node.right:
                track[node.val].add(node.right.val)
                get_childrens(node.right)
                
        get_childrens(root2)
        
        def can_be_flipped(node):
            
            if not node:
                return True
            
            cur, check = set(), True
            if node.left:
                cur.add(node.left.val)
                check = can_be_flipped(node.left)
            
            if node.right:
                cur.add(node.right.val)
                check &= can_be_flipped(node.right)
            

            if cur == track[node.val] and check:
                return True
            
            return False
        
        return can_be_flipped(root1)