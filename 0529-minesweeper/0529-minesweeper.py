class Solution:
    def updateBoard(self, grid: List[List[str]], click: List[int]) -> List[List[str]]:
        result = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),(-1, -1),(1, 1),(1, -1),(-1, 1)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        
        
        def dfs(grid, visited, row, col):
            
            if grid[row][col] == "M":
                
                grid[row][col] = "X"
                return
            
            visited[row][col] = True
            
            adj = []
            numofmine = 0

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row,new_col):
                    adj.append([new_row, new_col])
                
                if inbound(new_row,new_col) and grid[new_row][new_col] == "M":
                    numofmine += 1
            if numofmine:
                grid[row][col] = str(numofmine)
                return 
            else:
                grid[row][col] = "B"
                for new_row, new_col in adj:
                    if inbound(new_row, new_col) and not visited[new_row][new_col]:

                        dfs(grid, visited, new_row, new_col)
        
        dfs(grid, visited, click[0], click[1])
        return grid