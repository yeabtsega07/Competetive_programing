class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid: List[List[int]]) -> int:
        result = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        
        
        def dfs(grid, visited, row, col):

            
            visited[row][col] = True
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    
                    if grid[new_row][new_col]:

                        dfs(grid, visited, new_row, new_col)
        
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                
                if grid[i][j] and not visited[i][j] and not grid1[i][j]:
                    dfs(grid, visited, i, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] and not visited[i][j]:
                    dfs(grid, visited, i, j)
                    result += 1
        
    
        return result
        