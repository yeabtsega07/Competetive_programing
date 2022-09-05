# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=""
        head=l1
        while head:
            n1+=str(head.val)
            head=head.next
        n2=""
        while l2:
            n2+=str(l2.val)
            l2=l2.next   
        sum_=int(n1[::-1])+int(n2[::-1])
        sum_=str(sum_)
        sum_=sum_[::-1]
        Node = ListNode(int(sum_[0]))
        cur = Node
        i=1
        while i<len(sum_) and cur:
            cur.next=ListNode(int(sum_[i]))
            cur=cur.next
            i+=1
        return Node


           
            
            
            
        