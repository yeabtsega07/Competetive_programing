# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(91284,head)
        slow,fast=head,head.next
        
        while fast:
            if fast.val>slow.val:
                slow=fast
                fast=fast.next
                continue 
            check=dummy    
            while check.next.val<fast.val:
                check=check.next
            
            slow.next=fast.next
            fast.next=check.next
            check.next=fast
            fast=slow.next
        return dummy.next    
            