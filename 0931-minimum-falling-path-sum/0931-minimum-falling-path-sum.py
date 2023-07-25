class Solution:

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        
        def inBound( row, col ):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        dp = {}
        
        def recur ( row, col ):
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            if row == 0 and inBound(row, col):
                return matrix[row][col]
            
            if not inBound(row, col):
                return float("inf")
            
            topLeft = recur(row - 1, col - 1)
            top = recur(row - 1, col)
            topRight = recur(row - 1, col + 1)

            dp[(row, col)] = min(topLeft, top, topRight) + matrix[row][col]
            
            return dp[(row, col)]
        
        row, result = len(matrix) - 1, float("inf")
        
        for col in range(len(matrix[0])):
            result = min( recur(row, col), result)
        
        return result
            
            
            
            
            
            

        
        