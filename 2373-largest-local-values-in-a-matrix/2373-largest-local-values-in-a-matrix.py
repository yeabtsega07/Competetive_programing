class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        
        for i in range(n - 2):
            j, k = 0, 2
            max_ = 0
            cur = []
            while i + 2 < n and k < n:
                max_ = max(max(grid[i][j : k+1]), max(grid[i + 1][j:k+1]), max(grid[i + 2][j : k + 1]))
                k += 1
                j += 1
                cur.append(max_)
            
            if cur:
                ans.append(cur)
            
         
        return ans                   
                
                
        