class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        for i in range( 1, len(grid[0])):
            
            grid[0][i] += grid[0][i - 1]
            grid[1][i] += grid[1][i - 1]
        
        
        result = float("inf")
        
        for i in range( len(grid[0]) ):
            
            if i == 0:
                curVal = grid[0][-1] - grid[0][0]
            elif i == len(grid[0]):
                curVal = grid[1][i - 1]
            else:    
                curVal = max( grid[1][i - 1], grid[0][-1] - grid[0][i]  )
            
            result = min( result, curVal)
        
        return result
        