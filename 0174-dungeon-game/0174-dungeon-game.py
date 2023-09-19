class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        row, col = len(dungeon), len(dungeon[0])
        
        dp = [[float("inf")] * col for i in range(row)] 
        
        def inBound(r, c):
            return 0 <= r < row and 0 <= c < col
        
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):

                if i == row - 1 and j == col - 1:
                    if dungeon[i][j] < 0:
                        dp[i][j] = abs(dungeon[i][j]) + 1
                    else:
                        dp[i][j] = 1
                else:
                    bottom = float("inf") if not inBound(i + 1, j) else dp[i + 1][j]
                    right = float("inf") if not inBound(i, j + 1) else dp[i][j + 1]

                    
                    if dungeon[i][j] < 0: 
                        dp[i][j] = abs(dungeon[i][j]) + min( bottom, right)
                    else:
                        pre = min(bottom, right)
                        if pre <= dungeon[i][j]:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = pre - dungeon[i][j]
        

        return dp[0][0]
                        
                        