# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        
        visited = set()
        res = defaultdict(TreeNode)
        
        def inorder(root):

            if not root:
                return
            
            inorder(root.left)
            inorder(root.right)
            cur = []
            get_inorder(root,cur)
            cur = tuple(cur)
            if cur in visited:
                res[cur] = root
            
            visited.add(cur)
            
        
        def get_inorder(root, cur):
            
            if not root:
                cur.append(None)
                return
            
            get_inorder(root.left, cur)
            get_inorder(root.right,cur)
            cur.append(root.val)
            
        
        inorder(root)
        # print(res)
        return list(res.values())