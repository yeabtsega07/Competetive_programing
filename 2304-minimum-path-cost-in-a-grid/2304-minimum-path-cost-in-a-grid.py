class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        dp = {}
        
        def recur ( row, col ):
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            if row >= n or col >= m:
                return float("inf")
            
            if row == n - 1:
                return grid[row][col]
            
            res = float("inf")
            for i in range(m):
                
                if row + 1 < n: 
                    res = min(res, recur(row + 1, i) + moveCost[grid[row][col]][i])

            dp[(row, col)] = grid[row][col] + res
            
            return dp[(row, col)]
        
        result = float("inf")
        for i in range(m):
            
            result = min(result, recur(0, i))
        
        return result
            
            
        