# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        subtrees = defaultdict(int)
        result = []
        
        def preorder(root):
            
            if not root:
                return "Null"
            
            serial = ",".join([str(root.val), preorder(root.left), preorder(root.right)])
            if subtrees[serial] == 1:
                result.append(root)
            
            subtrees[serial] += 1
            
            
            return serial
        
        preorder(root)
        return result