class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        
        def inBound( row, col ):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        dir = [(1,0), (0, 1), (0, -1), (-1, 0)]
        

        
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0,0)])
        
        while heap:
            cur_val, cur_row, cur_col = heappop(heap)
            
            if cur_row == len(grid) - 1 and cur_col == len(grid[0]) - 1:
                return cur_val
            
            
            for change_r, change_c in dir:
                new_row = cur_row + change_r
                new_col = cur_col + change_c
                
                if inBound(new_row, new_col) and (new_row, new_col) not in visited :
                    val = max(cur_val , grid[new_row][new_col])
                    heappush(heap, (val, new_row, new_col))
                    visited.add((new_row, new_col))
        

            
                