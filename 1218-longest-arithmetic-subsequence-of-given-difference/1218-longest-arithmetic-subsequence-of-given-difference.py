class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = defaultdict(int)
        dp[len(arr) - 1] = 1
        res = 1
        
        for val in arr:
             
            dp[val] = dp[val - difference] + 1
            res = max(res, dp[val])
            
        return res
                        
                        