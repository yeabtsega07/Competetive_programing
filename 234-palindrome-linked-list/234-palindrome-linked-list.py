# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        right=len(res)-1    
        for i in range(len(res)-1):
            if i==right:
                break
            else:
                if res[i]!=res[right]:
                    return False
            right-=1
        return True    

    