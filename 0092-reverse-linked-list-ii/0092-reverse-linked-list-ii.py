# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        dummy = ListNode(-1)
        dummy.next = head
        cur, cnt = head, 1
        lPre , rNext = dummy, head
        
        while cur:
            if cnt < left:
                lPre = lPre.next
            if cnt == right:
                rNext = cur.next
                cur.next = None
                break
            cur = cur.next
            cnt += 1
        
        pre = lPre
        cur = pre.next
        nex = cur.next

        while nex:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        
        cur.next = rNext

        return dummy.next