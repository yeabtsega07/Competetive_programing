class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def inBound ( row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        dir  = [ (1,0), (0,1), (-1,0), (0,-1) ]
        visited = set()
        
        def bfs( row, col ):
            
            queue = deque([(row,col)])
            
            while queue:
                
                cur_row, cur_col = queue.popleft()
                
                for change_row, change_col in dir:
                    
                    new_row = cur_row + change_row
                    new_col = cur_col + change_col
                    
                    if inBound(new_row, new_col) and (new_row, new_col) not in visited:
                        if grid[new_row][new_col] == "1":
                            queue.append((new_row, new_col))
                            visited.add((new_row, new_col))
        
        result =  0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row, col) not in visited:

                    bfs(row, col)
                    result += 1
        
        return result
                
                               