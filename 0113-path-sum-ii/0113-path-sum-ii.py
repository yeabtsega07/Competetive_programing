# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        
        def recur(node,cur, track):
            
            if not node:
                return

            if not node.right and not node.left:
                if cur + node.val == targetSum:
                    track.append(node.val)
                    res.append(tuple(track))
                    track.pop()
                return
            
            track.append(node.val)
            recur(node.left, cur + node.val, track)
            recur(node.right, cur + node.val, track)
            track.pop()
        
        recur(root, 0, [])
        return res
                
            
            
    
            
            