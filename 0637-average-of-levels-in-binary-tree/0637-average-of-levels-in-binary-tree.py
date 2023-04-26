# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        levels = defaultdict(list)
        
        def bfs(node, level):
            visited = set([node, level])
            queue = deque([[node, level]])
            levels[level].append(node.val)
            while queue:
                node, level = queue.popleft()
                
                if node:
                    levels[level].append(node.val)
                
                    for neighbour in [node.left, node.right]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append([neighbour, level + 1])
        bfs( root, 0)
        ans = [0] * len(levels)
        for key, val in levels.items():
            
            ans[key] = sum(val) / len(val)
        
        return ans 
