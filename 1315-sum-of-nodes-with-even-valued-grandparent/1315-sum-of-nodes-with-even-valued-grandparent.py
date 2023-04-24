# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        track = []
        def dfs ( node, p = 0, gp = 0):
            if not node:
                return 
            
            if gp:
                track.append(node.val)
            
            if node.val % 2 == 0:
                gp = p
                p = 1
                dfs( node.left, p , gp )
                dfs( node.right, p , gp )

            else:
                gp = p
                p = 0
                dfs(node.left, p, gp)
                dfs( node.right, p , gp )
            
        dfs( root )
        return sum(track)