# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        result = []
        
        def dfs ( node, cur):
            
            if not node.left and not node.right:
                result.append( int( "".join(cur) ) )
                return
            
            if node.left:
                
                cur.append( str(node.left.val) )
                dfs( node.left, cur )
                cur.pop()
            
            if node.right:
                
                cur.append( str( node.right.val ) )
                dfs( node.right, cur )
                cur.pop()
        
        dfs( root , [str(root.val)])
        
        return sum( result )
        