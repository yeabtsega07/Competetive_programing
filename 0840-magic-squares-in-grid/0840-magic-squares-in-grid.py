class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nums = set(i for i in range(1,10))
        
        def check(i, j):
            
            if nums != set(grid[i + x][j + y] for x in range(3) for y in range(3)):
                return False
            
            sum_  = sum( grid[i][j + k] for k in range(3) )
            
            for x in range(3):
                if sum_ != sum( grid[i + x][ j + k ] for k in range(3)): 
                    return False
                
            for y in range(3):
                if sum_ != sum( grid[i + k][j + y] for k in range(3)):
                    return False
            
            if sum_ != sum(grid[i + k][j + k] for k in range(3)):
                return False
            
            if sum_ != sum(grid[i + k][j + 2 - k] for k in range(3)):
                return False
            
            return True
        
        row, col = len(grid), len(grid[0])
        result = 0
        
        for i in range(row - 2):
            for j in range(col - 2):
                
                result += check(i , j)
        
        return result
    