# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pt1, pt2, totalSum = l1, l2, ListNode()
        sum_ , carry = totalSum, 0
        
        while pt1 and pt2:
            
            if carry > 0:
                curSum = pt1.val + pt2.val + carry
            else:
                curSum = pt1.val + pt2.val 
            
            carry = 0
            if curSum // 10 > 0:
                carry = curSum // 10
                curSum %= 10 
                
            sum_.next = ListNode(curSum)
            sum_ = sum_.next
            pt1 = pt1.next
            pt2 = pt2.next
            
        while pt1:
            
            if carry > 0:
                curSum = pt1.val  + carry
            else:
                curSum = pt1.val 
            
            carry = 0
            if curSum // 10 > 0:
                carry = curSum // 10
                curSum %= 10 
            
            sum_.next = ListNode(curSum)
            sum_ = sum_.next
            pt1 = pt1.next
        
        while pt2:
            
            if carry > 0:
                curSum = pt2.val  + carry
            else:
                curSum = pt2.val 
            
            carry = 0
            if curSum // 10 > 0:
                carry = curSum // 10
                curSum %= 10 
            
            sum_.next = ListNode(curSum)
            sum_ = sum_.next
            pt2 = pt2.next
            
        if carry > 0:
            sum_.next = ListNode(carry)
            sum_ = sum_.next
        
        return totalSum.next
            
                
                
        
        