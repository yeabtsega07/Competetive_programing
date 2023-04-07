class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        self.count = 0
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            

            visited[row][col] = True
            
            for row_change, col_change in directions:
                
                new_row = row + row_change
                new_col = col + col_change
                if grid[row][col]:
                    
                    if not inbound(new_row, new_col):
                        self.count += 1
                    elif not grid[new_row][new_col]:
                        self.count += 1
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:  
                    dfs(grid, visited, new_row, new_col)
                    
                        
        dfs( grid, visited, 0, 0)
        return self.count