# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.get_middle(head)
        current = right.next
        right.next = None
        right = current
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def get_middle(self, root):
        
        slow, fast = root, root.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, left, right):
        pointer = dummy = ListNode()
        
        while left and right:
            
            if left.val <= right.val:
                pointer.next = left
                left = left.next
            else:
                pointer.next = right
                right = right.next
                
            pointer = pointer.next    
        if left:
            pointer.next = left
        if right:
            pointer.next = right
        
        return dummy.next