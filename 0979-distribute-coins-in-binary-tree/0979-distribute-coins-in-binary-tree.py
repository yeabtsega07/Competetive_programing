# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def dfs ( node ):
            
            if not node:
                return 0
            
            cur = dfs(node.left)
            cur += dfs(node.right)
            
            if node.val:
                cur += node.val - 1
            else:
                cur -= 1
                
            res[0] += abs(cur)
            
            return cur
        
        dfs(root)
        return res[0]
        
            
            