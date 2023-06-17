class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m ,  n = len(grid), len(grid[0])
        dp  = [ [-1] * n for _ in range(m)]
        
        def recur( i, j ):

            if i == 0 and j == 0 :
                return grid[i][j]
            
            if i < 0 or j < 0:
                return float("inf")
            
            if dp[i][j] != -1 :
                return dp[i][j]
            
            top , left = grid[i][j], grid[i][j]

            top += recur(i - 1, j)
            left += recur(i, j - 1)
            
   
            dp[i][j] = min(top, left)
            
            return dp[i][j]
        
        return recur(m - 1, n - 1)
        