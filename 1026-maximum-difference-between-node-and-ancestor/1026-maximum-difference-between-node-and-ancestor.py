# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        def dfs (root, max_ , min_ ):
            
            if root:
                self.res = max(max_-root.val, root.val - min_, self.res) 
                max_ = max(max_, root.val)
                min_ = min(min_, root.val)
                # print(root.val)
                dfs(root.left, max_, min_)
                dfs(root.right,max_,min_)
                    
        
            
        dfs(root, root.val, root.val)
        return self.res    
                
                
            