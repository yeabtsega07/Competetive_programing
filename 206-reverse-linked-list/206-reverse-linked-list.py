# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur_val=head
        previous=None
        while cur_val:
            next=cur_val.next
            cur_val.next=previous
            previous=cur_val
            cur_val=next   
        head=previous
        return head 
        