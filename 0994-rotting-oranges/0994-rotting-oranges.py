class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dirc = [(0,1), (1, 0), (0, -1), (-1, 0)]
        
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        result, count = 0, 0
        queue = deque([])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 2:
                    queue.append((row, col))
                
                if grid[row][col] == 1:
                    count += 1
        
        if not count:
            return 0
        
        
        while queue and count:
            
            for _ in range(len(queue)):
                
                cur_row, cur_col = queue.popleft()
                
                for change in dirc:
                    new_row = cur_row + change[0]
                    new_col = cur_col + change[1]
                    
                    if inBound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        count -= 1
            
            result += 1
        
        return result if not count else -1
                    
        