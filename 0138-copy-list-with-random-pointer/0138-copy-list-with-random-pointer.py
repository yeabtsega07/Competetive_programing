"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return 
        
        track = {}
        
        def clone (node):
            
            if not node:
                return 
            if node in track:
                return track[node]
            
            newNode = Node(node.val)
            track[node] = newNode
            
            newNode.next = clone(node.next)
            newNode.random = clone(node.random)
            
            
            return track[node]
        
        clone(head)
        return track[head]
                
                
            
            
        
        