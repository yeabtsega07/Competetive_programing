class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        
        def recur(ind):
            if ind == 0:
                return nums[ind]
            if ind < 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            pick = nums[ind] + recur(ind-2)
            nonPick = 0 + recur(ind-1)
            dp[ind] = max(pick, nonPick)
            
            return dp[ind]
    
        return recur(len(nums) -  1)
            
        