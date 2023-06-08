class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = defaultdict(int)
        
        def recur( i, j ):
            
            if i == 0 and j ==  0:
                return 1
            
            if i < 0 or j < 0:
                return 0
            
            if dp[(i,j)]:
                return dp[(i,j)]
            
            left = recur( i, j - 1 )
            top = recur( i - 1, j )
            dp[(i, j)] = left + top
            
            return dp[(i,j)]
        
        return recur(m - 1, n - 1)
            