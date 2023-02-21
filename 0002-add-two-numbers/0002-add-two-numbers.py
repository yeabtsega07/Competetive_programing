# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        check = l1
        while check:
            num1.append(str(check.val))
            check = check.next
        
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next    
        
        num1 = int("".join(num1)[::-1])
        num2 = int("".join(num2)[::-1])
        num1 = num1 + num2
        num1, index = str(num1), 0
        num1 = num1[::-1]
        
        l = ListNode()
        check = l
        while index < len(num1):
            
            check.next = ListNode(int(num1[index]))
            check = check.next
            index += 1
            
        return l.next
        