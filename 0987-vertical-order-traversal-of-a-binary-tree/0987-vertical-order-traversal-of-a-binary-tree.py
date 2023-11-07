# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        columns = defaultdict(list)
        
        queue = deque([(root, 0, 0)])
        
        while queue:
            
            current_node, current_col, level = queue.popleft()
            
            columns[current_col].append((level, current_node.val))
            
            if current_node.left:
                queue.append((current_node.left, current_col - 1, level + 1))
            
            if current_node.right:
                queue.append((current_node.right, current_col + 1, level + 1))

        result = []
        for col, values in sorted(columns.items()):
            cur = [val[1] for val in sorted(values)]
            result.append(cur)
            
        return result