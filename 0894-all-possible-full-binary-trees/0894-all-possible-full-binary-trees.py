# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n %2 == 0:
            return []
        
        @lru_cache
        def helper(m): 
            if m == 1:
                return [TreeNode(0)]
            elif m >1:
                res = []
                for i in range(1, m, 2):
                    
                    candleft = helper(i)
                    candright = helper(m-1-i)
                    for l in candleft:
                        for r in candright:
                            node = TreeNode(0)
                            node.left = l
                            node.right = r
                            res.append(node)
                return res
                
        return helper(n)
        