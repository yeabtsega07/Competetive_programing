class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def inBound(row, col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])
        
        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        pac, atl = set(), set()
        
        def dfs (row, col, visited, pre):
            
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            
            for change_row, change_col in dir:
                
                new_row = row + change_row
                new_col = col + change_col
                
                if inBound(new_row, new_col) and (new_row, new_col) not in visited:

                    if heights[new_row][new_col] >= pre:
                        dfs(new_row, new_col, visited, heights[new_row][new_col])
        
        for col in range(len(heights[0])):
            
            dfs(0, col, pac, heights[0][col])
            dfs(len(heights) - 1, col, atl, heights[len(heights) - 1][col])
        
        for row in range(len(heights)):
            
            dfs(row, 0, pac, heights[row][0])
            dfs(row, len(heights[0]) - 1, atl, heights[row][len(heights[0]) - 1])
        
        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                
                if (row, col) in pac and (row, col) in atl:
                    res.append((row, col))
        
        return res