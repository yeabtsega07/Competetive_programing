class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = grid[sr][sc]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(grid, visited, row, col):

            visited[row][col] = True
            
            for row_change, col_change in directions:
                
                new_row = row + row_change
                new_col = col + col_change

                if grid[row][col] == start:
                    grid[row][col] = color
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    
                    if grid[new_row][new_col] == start:
                        grid[new_row][new_col] = color
                        dfs(grid, visited, new_row, new_col)
                    
                    
        
        dfs( grid, visited, sr, sc)
        return grid