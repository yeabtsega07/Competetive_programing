class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        sLen, tLen = len(s), len(t)
        
        if sLen < tLen:
            return 0
        
        dp = [[0] * (sLen + 1) for _ in range(tLen + 1)]
        dp[0] = [1] * (sLen + 1)
        
        for i in range(1, tLen + 1):
            for j in range(1, sLen + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        return dp[tLen][sLen]