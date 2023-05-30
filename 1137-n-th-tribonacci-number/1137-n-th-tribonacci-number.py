class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = {0:0,1:1,2:1}
        
        def recur(n):
            if n not in dp:
                dp[n] = recur(n - 3) + recur(n - 2) + recur(n - 1)
            
            return dp[n]
        
        return recur(n)
        