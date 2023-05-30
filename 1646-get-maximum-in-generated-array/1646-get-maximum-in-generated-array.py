class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        dp = {0:0,1:1}
        def recur(n):
            if n not in dp:
                if n % 2 == 0:
                    dp[n] = recur(n // 2)
                else:
                    dp[n] = recur(n // 2) + recur( (n // 2) + 1)
            
            return dp[n]
        
        for i in range(2, n + 1):
            recur(i)

        return max(dp.values()) if n > 0 else 0
                    