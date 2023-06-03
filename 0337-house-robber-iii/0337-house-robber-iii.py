# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        dp = defaultdict(int)
        
        def recur ( node ):
            
            if not node:
                return 0
            
            if dp[node]:
                return dp[node]
            
            pick = node.val
            notpick = 0
            if node.left:
                pick += recur(node.left.left) + recur(node.left.right)
                notpick += 0 + recur(node.left)
            
            if node.right:
                pick += recur(node.right.right) + recur(node.right.left)
                notpick += 0 + recur(node.right)

            dp[node] += max(pick,notpick)    

            return dp[node]

        return recur( root )