class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        for i in range( len(nums)):
            
            take = nums[i]  
            if i > 1:
                take += dp[i - 2] 
            nonTake = 0 + dp[i - 1]
            
            dp[i] = max(take, nonTake)
        
        return dp[len(nums) - 1]
             
        