# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        check=head
        prev=None
        cur=head
        comp=[]
        while check:
            comp.append(check.val)
            check=check.next
     
        while cur:
            tail=cur.next
            cur.next=prev
            
            prev=cur
            cur=tail
        an=[]
        while prev:
            an.append(prev.val)
            prev=prev.next
        return comp==an        