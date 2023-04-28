class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        path = []
        
        def bfs(grid, row, col):
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(1,1),(-1,-1),(-1,1),(1,-1)]
            
            visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
            def inbound(row, col):
                return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
            
            queue = deque([[row, col ,0]])
            
            while queue:
                
                row, col, count = queue.popleft()

                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    path.append(count)
                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                
                    if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        
                        if grid[new_row][new_col] == 0:
                            visited[new_row][new_col] = True
                            queue.append([new_row, new_col, count + 1])
        
        if not grid[0][0]:
             bfs( grid, 0, 0)
                
        return path[0] + 1 if path else -1
                        
                        