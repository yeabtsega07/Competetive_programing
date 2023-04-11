# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        res = []
        
        def dfs ( node, visited ):
            
            if not node:
                return
            
            visited.add(node)
            res.append(str(node.val))
            
            if node.left and node.left not in visited:
                res.append("(")
                dfs(node.left, visited)
                res.append(")")
            
            if not node.left and node.right:
                res.append("()")
                
            if node.right and node.right not in visited:
                    
                res.append("(")    
                dfs(node.right, visited)
                res.append(")")
        
        dfs( root, set())
    
        
        return "".join(res)
        