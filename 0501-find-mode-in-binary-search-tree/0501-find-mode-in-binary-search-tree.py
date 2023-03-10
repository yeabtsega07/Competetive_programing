# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        nodes = []
        
        def inorder( root ):
            
            if not root:
                return
            
            nodes.append(inorder(root.left))
            nodes.append(root.val)
            nodes.append(inorder(root.right))
        
        inorder( root )
        check = Counter(nodes)
        check.pop(None)
        
        result, val = [], max(check.values())
        for key in check:
            if check[key] == val:
                result.append(key)
        return result        