class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def bfs ( grid, row, col ):
            
            def inbound(row, col):
                return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
            
            directions = [ (1,0), (0,1), (-1,0), (0,-1)]
            
            queue = deque([(row, col, 0)])
            visited = set([(row, col)])

            
            while queue :

                row, col, count = queue.popleft()
                
                if row == 0 or col == 0 or row  == len(grid) - 1 or col  == len(grid[0]) - 1:
                    
                    if [row, col] != entrance:
                        return count

                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if inbound( new_row, new_col ) and (new_row, new_col) not in visited:
                        
                        if grid[new_row][new_col] != "+":
                            queue.append((new_row, new_col, count + 1))
                            visited.add((new_row, new_col))
            

            return -1
        
        
        return (bfs( maze, entrance[0], entrance[1] ))
                
            