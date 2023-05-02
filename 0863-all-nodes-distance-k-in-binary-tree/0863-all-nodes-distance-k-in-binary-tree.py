# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def traverse( root ):
            
            if not root:
                return
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                traverse( root.left )
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                traverse( root.right )
        
        traverse( root )
        
        queue = deque([[target.val, 0]])
        visited = set([target.val])
        res = []

        while queue:
            
            node, count = queue.popleft()

            if count == k:

                res.append(node)

            for child in graph[node]:

                if child not in visited:
                    
                    visited.add(child)
                    queue.append([child, count + 1])
        
        return res
                
        