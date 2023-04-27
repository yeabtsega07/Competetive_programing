class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):

            
            visited[row][col] = True
            
              
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col] :
                    
                    if grid[new_row][new_col] == "O":
                        dfs( grid, visited, new_row, new_col)
                    
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if (i == len(grid) - 1 or j == len(grid[i]) - 1 or i == 0 or j == 0) and grid[i][j] == "O" and grid[i][j] not in visited:
                    
                    dfs( grid, visited, i, j )
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == "O" and not visited[i][j]:
                    grid[i][j] = "X"
        
        
                
                