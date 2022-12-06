# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy = ListNode(1, head)
        length = 0
        
        while dummy:
            length += 1
            dummy = dummy.next
        
        check = (length - 1) // k
        rem = 0
        if check:
             rem = (length - 1) % k
        else:
            check = 1
        ans, pre, count = [], head, 0
        
        while head:
            count += 1
            # print(count,check)
            if  rem :
                if count == check + 1:
                    tail = head.next
                    head.next = None
                    ans.append(pre)
                    pre = tail
                    cur = []
                    k -= 1
                    count = 0
                    head = pre
                    rem -= 1
                    continue
            else:        
                if count == check:
                    tail = head.next
                    head.next = None
                    ans.append(pre)
                    pre = tail
                    cur = []
                    k -= 1
                    count = 0
                    head = pre
                    continue
                
            head = head.next    
            
            
        
        
        while k:
            ans.append(None)
            k -= 1
        return ans    
            
            
        