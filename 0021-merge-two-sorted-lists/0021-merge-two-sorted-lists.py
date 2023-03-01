# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy    
        def recur():
            nonlocal list1
            nonlocal list2
            nonlocal dummy
            nonlocal tail 
            
            if not list1 or not list2 : return
            
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next    
            
            recur()
        
        recur()
        if list1:

            tail.next = list1
        else:

            tail.next = list2
        
        return dummy.next
        
        
        
            
                
                
        