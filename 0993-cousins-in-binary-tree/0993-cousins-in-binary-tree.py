# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        depth = defaultdict(tuple)
        
        def recur(root, row, parent):
            
            if not root:
                return 
            
            if root.val == x or root.val == y:
                depth[root.val] = (row, parent)
            
            recur(root.left, row + 1, root.val)
            recur(root.right, row + 1, root.val)
        
        recur(root, 0, -1)

        return depth[x][0] == depth[y][0] and depth[x][1] != depth[y][1] 