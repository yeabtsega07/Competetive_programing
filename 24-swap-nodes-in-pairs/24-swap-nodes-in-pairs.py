# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        pt1=dummy
        pt2=head
        while pt2 and pt2.next:
            tail=pt2.next.next
            nxt=pt2.next
            
            nxt.next=pt2
            pt2.next=tail
            pt1.next=nxt
            
            pt1=pt2
            pt2=tail
        return dummy.next   