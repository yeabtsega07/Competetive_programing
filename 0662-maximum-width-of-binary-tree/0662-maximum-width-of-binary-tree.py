# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        track, maxWidth = deque(), 0
        track.append([0, root])
        
        while track :
            
            level = []
            

            for i in range(len(track)):
                
                val , node = track.popleft()
                

                level.append(val)
                
                if node:
                    track.append( [2 * val + 1, node.left])
                    track.append([2 * val + 2, node.right])


            
            maxWidth = max(maxWidth, max(level) - min(level) + 1)
            

            
        return maxWidth // 2
                
            