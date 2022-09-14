# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next    
        # if fast:
        #     return head
        test=slow
        pre=None
        while test:
            nxt=test.next
            test.next=pre
            pre=test
            test=nxt
        # test=head    
        # while test.next and test.next.next:
        #     test=test.next
        # test.next=test.next.next
        top=head
        mid=pre
        while top:
            nxt=top.next
            top.next=mid
            nxt2=mid.next
            mid.next=nxt
            top=nxt
            mid=nxt2
        # if mid:
        #     test=head
        #     while test.next:
        #         test=test.next
        #     test.next=mid    
            
            
        