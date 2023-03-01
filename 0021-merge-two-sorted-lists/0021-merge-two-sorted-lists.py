# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and list2:
            return list2
        elif not list2 and list1: 
            return list1
        elif not list1 and not list2: 
            return None
        
        dummy = ListNode()
        
        if list1.val <= list2.val:
            dummy.val = list1.val
            list1 = list1.next
        else:
            dummy.val = list2.val
            list2 = list2.next
        
        dummy.next = self.mergeTwoLists(list1, list2)
        
        return dummy
        
        
        
        
            
                
                
        