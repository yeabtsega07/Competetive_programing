# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        track = defaultdict(list)
        tree = defaultdict(TreeNode)
        
        def traverse (node, parent):
            if not node:
                return
            tree[node.val] = node
            if parent in track:
                track[node.val] = track[parent] + [node.val]
            else:
                track[node.val] = [node.val]
            
            traverse(node.left, node.val)
            traverse(node.right, node.val)
        
        traverse(root, root.val)
        anst_p, anst_q = 0, 0

        while anst_p < len(track[p.val]) and anst_q < len(track[q.val]) and track[p.val][anst_p] == track[q.val][anst_q]:

            anst_p += 1
            anst_q += 1
            
        return tree[track[p.val][anst_p - 1]]    