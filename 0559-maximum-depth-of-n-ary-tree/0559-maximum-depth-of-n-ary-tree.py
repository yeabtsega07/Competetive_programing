"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        self.ans = 0
        def dfs (node, visited, count):
            
            self.ans = max( self.ans, count )
            
            if not node:
                return 
            
            visited.add(node)
            
            for child in node.children:
                
                if child not in visited:
                    
                    dfs(child, visited, count + 1)
                    

                    
                    
        
        dfs(root, set(), 1)
        return self.ans
            
            
        