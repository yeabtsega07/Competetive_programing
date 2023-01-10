class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        top, rear = 0, len(matrix)
        lft, rgt = 0, len(matrix[0])
        while lft < rgt and top<rear:
            for i in range (lft, rgt):
                out.append(matrix[top][i])
            top += 1    
            for i in range(top, rear):
                out.append(matrix[i][rgt-1])
            rgt -= 1
            if not(lft < rgt and top < rear):
                break

            for i in range (rgt-1, lft-1, -1):
                out.append(matrix[rear-1][i])
            rear -= 1    
            for i in range(rear-1, top-1, -1):
                out.append(matrix[i][lft])
            lft += 1
        return out    
        