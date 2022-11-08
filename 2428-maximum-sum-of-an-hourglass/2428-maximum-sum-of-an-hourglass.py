class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # prefix sum
        n = len(grid[0])
        maxSum = 0
        for i in range(1,len(grid)-1):
            for j in range(1,n-1):
                curSum = sum(grid[i-1][j-1:j+2]) +grid[i][j] + sum(grid[i+1][j-1:j+2])
                maxSum = max(maxSum, curSum)
        
        return maxSum
                
                    
                
            
        