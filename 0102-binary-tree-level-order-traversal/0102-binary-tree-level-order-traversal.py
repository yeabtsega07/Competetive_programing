# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         result = []
        
#         levels = deque()
#         levels.appendleft(root)
        
#         while levels:
            
#             level = []
#             for i in range(len(levels)):
                
#                 node = levels.popleft()
#                 if node:
#                     level.append(node.val)
#                     levels.append(node.left)
#                     levels.append(node.right)
                    
#             if level :      
#                 result.append(level)
        
#         return result             
                    
          
        levels = defaultdict(list)
        if not root:
            return levels
        
        def traverse (root, levels, level):
            
            levels[level].append(root.val)  
            if root.left:
                traverse(root.left, levels, level + 1)
            if root.right:
                traverse(root.right, levels, level + 1)
            
        traverse(root, levels, 0)
        return levels.values()
        
            