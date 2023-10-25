class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # dppppppppppppppppppp
        
        empty_count = 0
        start  = ()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if not grid[i][j]:
                    empty_count += 1
                elif grid[i][j] == 1:
                    start = (i, j)
        
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        dir = [(0,1),(1, 0), (-1, 0), (0, -1)]
        
        count = [0]
        dp = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        
        def recur( row, col):
            
            if not inBound(row, col) or  dp[row][col] or grid[row][col] == -1 :
                return 

            
            if grid[row][col] == 2:
                cur_count = 0

                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        
                        if dp[i][j]:
                            cur_count += 1

                if cur_count == empty_count + 1:
                    count[0] += 1
            
                return
                       
            dp[row][col] = 1
            for change in dir:
                new_r = row + change[0]
                new_c = col + change[1]
                
                recur(new_r, new_c)
            
            dp[row][col] = 0
            
            return
        
        recur(start[0], start[1])
        return count[0]
            
                
                    
        
        