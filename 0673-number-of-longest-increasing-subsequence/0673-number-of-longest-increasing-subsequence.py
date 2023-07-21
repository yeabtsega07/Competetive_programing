class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp = {}
        maxLen, res = 0, 0
        
        for i in reversed(range(len(nums))):
            
            cur = count = 1
            
            for j in range(i + 1, len(nums)):
                
                if nums[i] < nums[j]:

                    if dp[j][0] + 1 > cur:
                        cur, count = dp[j][0] + 1, dp[j][1]
                    elif dp[j][0] + 1 == cur:
                        count += dp[j][1]
                        
            if cur > maxLen:
                maxLen, res = cur, count
            elif cur == maxLen:
                res += count
            
            dp[i] = (cur,count)   

        return res
        
            
            
            
            
                
        