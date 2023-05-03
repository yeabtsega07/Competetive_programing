class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        queue = deque()
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
         
        def dfs(grid, visited, row, col):

            visited[row][col] = True
            
            if grid[row][col]:
                queue.append([row, col, 0])

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                
                
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    
                    if grid[new_row][new_col]:
                        dfs(grid, visited, new_row, new_col)
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                check = 0                
                if grid[i][j]:
                    dfs(grid, visited, i, j)
                    check = 1
                    break
            if check:
                break        

        

            
        while queue:

            row, col, count = queue.popleft()


            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change 

                if inbound(new_row, new_col) and not visited[new_row][new_col] :
                    
                    if grid[new_row][new_col]:
                        return count

                    visited[new_row][new_col] = True
                    queue.append([new_row, new_col, count + 1])
            

            
                        