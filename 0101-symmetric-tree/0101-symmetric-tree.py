# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        levels = deque()
        levels.appendleft(root)
        
        while levels:
            
            level = []
            for i in range(len(levels)):
                
                node = levels.popleft()
                if node:
                    level.append(node.val)
                    levels.append(node.left)
                    levels.append(node.right)
                else:
                    level.append(None)
            

            if level and level != level[::-1]:
                return False
                
        return True