class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        dp = {len(nums) - 1 : 1}
        
        for i in reversed(range(len(nums) - 1)):
            
            cur = 1
            for j in range(i + 1, len(nums)):
                
                if nums[i] < nums[j]:

                    cur = max(cur, 1 + dp[j])
            
            dp[i] = cur    
        
        return max(dp.values())
        