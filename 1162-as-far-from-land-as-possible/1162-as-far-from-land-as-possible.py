class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        track = defaultdict(int)
        queue = deque()
        N = len(grid)
        
        def inBound (row, col):
            return 0 <= row < N and 0 <= col < N
        
        for row  in range(N):
            for col in range(N):
                
                if grid[row][col]:
                    queue.append((row, col))
                    track[(row, col)] = -1
        level = 0 
        while queue:
            
            for _ in range(len(queue)):
                
                row, col = queue.popleft()
                
                
                for r,c in directions:
                    new_row = row + r
                    new_col = col + c
                    
                    if (new_row, new_col) not in track and inBound(new_row, new_col):
                        queue.append((new_row, new_col))
                        track[(new_row, new_col)] = level + 1
            level += 1
        return max(track.values()) if track else -1
                    
        