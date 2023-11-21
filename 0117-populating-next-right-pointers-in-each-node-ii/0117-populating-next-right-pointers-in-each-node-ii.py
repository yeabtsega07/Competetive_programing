"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        level order travsesal BFS O(N) time and O(N) space
        
        """
        if not root:
            return

        queue = deque([root])
        
        while queue:
            prev = None
            
            for i in range(len(queue)):
                cur = queue.popleft()
                
                if prev:
                    prev.next = cur
                
                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)
                
                prev = cur
                
        return root        