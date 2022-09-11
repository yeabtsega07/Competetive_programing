# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow = slow.next   
            
        pre=None
        while slow:
            nxt=slow.next
            slow.next=pre
            pre=slow
            slow=nxt
        top,mid=head,pre

        while mid:
            if top.val!=mid.val:
                return False
            mid=mid.next
            top=top.next
        return True    
    