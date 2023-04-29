class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
         
        def bfs( ):
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
            def inbound(row, col):
                return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
            
            queue = deque()
            
            for i in range( len(grid) ):
                for j in range( len(grid[0]) ):
                    
                    if grid[i][j] == 0: 
                        queue.append((i, j))
                        visited[i][j] = True
                    else:
                        grid[i][j] = -1
            
            while queue:
                
                row, col = queue.popleft()
                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                
                    if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        
                        grid[new_row][new_col] =  grid[row][col] + 1

                        visited[new_row][new_col] = True
                        queue.append([new_row, new_col])
        
            
    
    
        bfs()
        return grid
                        