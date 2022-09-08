# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        list_=[]
        while head:
            list_.append(head.val)
            head=head.next
            
        mon_stack=[]
        res=[0]*len(list_)
        for i , num in enumerate(list_):
            while mon_stack and list_[mon_stack[-1]]<num:
                ind=mon_stack.pop()
                res[ind]=num
            mon_stack.append(i)
        return res    
                
        