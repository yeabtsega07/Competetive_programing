# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length, check = 0, head
        
        while check:
            check = check.next
            length += 1
        
        if length == 0:
            return head
        
        while k > length:
            k %= length
        
        count, pt = 0, head
        
        while pt:
            
            if length - count == k:
                break
            pt = pt.next
            count += 1
        
        part1, part2 = ListNode(), ListNode()
        pt1, pt2, check = part1, part2, pt
        
        while head != check:
            
            pt1.next = head
            pt1 = pt1.next
            head = head.next
        pt1.next = None    
        
        while pt:
            
            pt2.next = pt
            pt2 = pt2.next
            pt = pt.next
            
        pt2.next = part1.next
        
        return part2.next
            