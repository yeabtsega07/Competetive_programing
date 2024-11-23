class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        Row, Col = len(grid), len(grid[0])
        directions = [(1,0), (0, 1), (0, -1), (-1, 0)]
        def inBound(row, col):
            return 0 <= row < Row and 0 <= col < Col
        visited = [[False for _ in range(Col) ] for _ in range(Row)]
        
        def dfs( row, col ):
            
            visited[row][col] = True
            
            for direction in directions:
                new_row, new_col = row + direction[0], col + direction[1]
                if inBound(new_row, new_col) and grid[new_row][new_col] == "1":
                    if not visited[new_row][new_col]:
                        dfs(new_row, new_col)
            
        
        count = 0
        for row in range(Row):
            for col in range(Col):
                
                if grid[row][col] == "1":
                    if not visited[row][col]:
                        dfs(row, col)
                        count += 1
        
        return count
        