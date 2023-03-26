# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        counts = []
        prefix = defaultdict(int)
        prefix[0] += 1
        
        def traverse ( root, cur_sum = 0, track = [] ):
            
            if not root:
                return
            
            cur_sum += root.val
            track.append(root.val)
            counts.append(prefix[ cur_sum - targetSum ])

            prefix[cur_sum] += 1
            
            traverse( root.left, cur_sum )
            traverse( root.right, cur_sum )
            
            prefix[cur_sum] -= 1
            
        
        traverse( root )
        return sum(counts)
            
    