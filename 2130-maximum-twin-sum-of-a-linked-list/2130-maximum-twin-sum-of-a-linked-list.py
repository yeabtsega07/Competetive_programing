# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        pre=None
        while slow:
            nxt=slow.next
            slow.next=pre
            pre=slow
            slow=nxt
         
        mid,top=pre,head
        max_=0
        while mid:
            max_=max(mid.val+top.val,max_)
            mid=mid.next
            top=top.next
        return max_    
        