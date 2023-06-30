class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = defaultdict(int)
        
        def recur ( row, col ):
            
            if row == len(triangle) - 1:
                return triangle[row][col]
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            down = triangle[row ][col] + recur(row + 1, col)
            diagonal = triangle[row][col] + recur(row + 1, col + 1)
            dp[(row, col)] = min(down, diagonal)
            
            return dp[(row, col)]
        
        return recur(0, 0)
        
        