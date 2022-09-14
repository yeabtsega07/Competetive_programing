# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            pre=slow
            slow=slow.next
        if not pre:
            return head.next
        pre.next=slow.next
        return head
        