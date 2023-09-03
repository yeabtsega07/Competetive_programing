class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        
        def recur( row, col):
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            if row < 0 or col < 0:
                return 0
            
            if row == 0 and col == 0:
                return 1
            
            top = recur(row - 1, col)
            left = recur(row, col - 1)
            
            dp[(row, col)] = top + left
            
            return dp[(row, col)]
        
        return recur(m - 1, n - 1)