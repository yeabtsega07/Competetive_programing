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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        leftMost = root
        
        while leftMost:
            
            cur = leftMost
            leftMost = None
            pre = None
            
            while cur:
                
                if cur.left:
                    if not leftMost:
                        leftMost = cur.left
                    
                    if pre:
                        pre.next = cur.left
                    
                    pre = cur.left
                
                if cur.right:
                    
                    pre.next = cur.right
                    pre = cur.right
                
                cur = cur.next
        
        return root
                        
                        