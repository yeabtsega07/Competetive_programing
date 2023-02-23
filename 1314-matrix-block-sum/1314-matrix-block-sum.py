class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        matrix = mat
        matrix.append([0] * len(mat[0])) 
        
        for row in matrix:
            row.append(0)
        
        for  row in range(len(matrix) - 1):
            for col in range(len(matrix[0]) - 1):
                
                top = matrix[row - 1][col]
                left = matrix[row][col - 1]
                topLeft = matrix[row - 1][col - 1]
                
                matrix[row][col] +=  top + left  -  topLeft
        def sumRegion(row1: int, col1: int, row2: int, col2: int, matrix = matrix) -> int:
        
            left = matrix[row2][col1 - 1] 
            top = matrix[row1 - 1][col2]
            topLeft = matrix[row1 - 1][col1 - 1]
            bottomG = matrix[row2][col2]

            return bottomG - left - top + topLeft        
                
        ans = [] 
        
        for r in range(len(matrix) - 1):
            row = []
            for c in range(len(matrix[0]) - 1):
                r1, c1 = max(0, r - k), max(0, c - k)
                r2, c2 = min(len(matrix) - 2, r + k), min(len(matrix[0]) - 2, c + k)
                row.append(sumRegion(r1, c1, r2, c2))
            
            ans.append(row)
        return ans    
                