# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lNode, rNode = left, right
        
        while head:
            
            if head.val < x:
                lNode.next = head
                lNode = lNode.next
            elif head.val >= x:
                rNode.next = head
                rNode = rNode.next
                
            head = head.next

        lNode.next = right.next
        rNode.next = None

        return left.next