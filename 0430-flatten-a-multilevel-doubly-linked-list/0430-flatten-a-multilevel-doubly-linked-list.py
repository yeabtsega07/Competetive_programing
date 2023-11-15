"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def recur (current, parent):

            if not current:
                return
            
            if parent:
                current.prev = parent
                parent.next = current
                

                
            while current.next and not current.child: 
                current = current.next

            if current and current.child:
                next_list = current.next
                node = recur( current.child, current)
                current.child = None
                if next_list:
                    next_list.prev = node
                    node.next = next_list
                    
            
            while current.next and not current.child:
                current = current.next
            
            return current
        
        dummy = head
        recur(dummy, None)

        return head
            
            