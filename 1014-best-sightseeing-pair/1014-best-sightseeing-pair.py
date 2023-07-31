class Solution:
    def maxScoreSightseeingPair(self, nums: List[int]) -> int:
        
        left = nums[0]
        res = -float("inf")
        
        for i in range(1, len(nums)):
            
            res = max( res, left + nums[i] - 1)
            left = max( left - 1 , nums[i])
        
        return res