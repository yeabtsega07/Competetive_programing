# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_=head
        dict={}
        while node_:
            if node_ in dict:
                return True
            dict[node_]=1
            node_=node_.next
        return False   