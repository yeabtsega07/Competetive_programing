class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def inBound ( row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        dir  = [ (1,0), (0,1), (-1,0), (0,-1) ]
        visited = set()
        
        def dfs (row, col):
            
            
            visited.add((row, col))
            for point in dir:
                
                newcol = col + point[1]
                newrow = row + point[0]
                
                if inBound(newrow, newcol) and (newrow, newcol) not in visited:
                    if grid[row][col] == "1":
                        dfs(newrow, newcol)
        
        result =  0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row, col) not in visited:

                    dfs(row, col)
                    result += 1
        
        return result
                
                               