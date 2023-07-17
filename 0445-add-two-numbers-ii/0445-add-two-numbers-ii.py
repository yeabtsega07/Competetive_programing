# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse (head):
            pre = None
            cur = head

            while cur :
                    
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                
                

            head = pre
            return head
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        res = ListNode(0)
        p1, p2, p3 = l1, l2, res
        
        while p1 and p2:
            
            cur = p1.val + p2.val
            if cur // 10:
                if p1.next:
                    p1.next.val += 1
                    cur %= 10
                elif p2.next:
                    p2.next.val += 1
                    cur %= 10 
                else:
                    p3.next = ListNode(cur % 10) 
                    p3 = p3.next 
                    cur = cur // 10
                    
            p3.next = ListNode(cur) 
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            
            if p1.val // 10:
                if p1.next:
                    p1.next.val += 1
                    p1.val %= 10
                else:    
                    p3.next = ListNode(p1.val % 10) 
                    p3 = p3.next 
                    p1.val = p1.val // 10
                    
            p3.next = ListNode(p1.val)
            p3 = p3.next
            p1 = p1.next
        
        while p2:
            
            if p2.val // 10:
                if p2.next:
                    p2.next.val += 1
                    p2.val %= 10
                else:    
                    p3.next = ListNode(p2.val % 10) 
                    p3 = p3.next 
                    p2.val = p2.val // 10
                
            p3.next = ListNode(p2.val)
            p3 = p3.next
            p2 = p2.next
        
        
        res = reverse(res.next)
        return res
            
            
            
        
        