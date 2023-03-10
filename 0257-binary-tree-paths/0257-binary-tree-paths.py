# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        paths = set()
        
        def preorder( root, path, paths ):
            
            path.append(str(root.val))
            
            if not root.left and not root.right:
                paths.add('->'.join(path))

            if root.left:
                preorder(root.left, path, paths)
            if root.right:    
                preorder(root.right, path, paths)
            
            if path:
                path.pop()
            
            return paths
        
        return preorder(root, [], paths)

            
            
        