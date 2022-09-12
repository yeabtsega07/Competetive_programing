# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(777,head)
        pre=dummy
        while head:
            if head.next and head.val==head.next.val:

                while head.next and head.val==head.next.val:
                    head=head.next
                pre.next=head.next
            else:
                pre=pre.next

            head=head.next
                   
        return dummy.next        
                