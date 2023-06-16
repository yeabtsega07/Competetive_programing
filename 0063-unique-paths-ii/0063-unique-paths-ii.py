class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
    
        
        dp = defaultdict(int)
        n , m = len(grid[0]), len(grid)
        
        # exception
        if grid[m - 1][n - 1]:
            return  0
        
        def recur ( i, j ):
            
            if i == 0 and j  == 0:
                return 1
            
            if dp[(i, j)]:
                return dp[(i,j)]
            
            top, left = 0 , 0
                
            if 0 <= i - 1 < m  and not grid[i - 1][j]:
                top = recur(i - 1, j)
            
            if 0 <= j - 1 <n and not grid[i ][j - 1]:
                left = recur(i, j - 1)
            
            # print(left, top)
            dp[(i, j)] = left + top
            
            return dp[(i,j)]
        # print(dp)    
        return recur(m - 1, n - 1)
        