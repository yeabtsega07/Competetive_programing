class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        curMax = nums[0]
        track = nums[0]
        
        for i in range(1 , len(nums)):
            track += nums[i]
            curMax = max(curMax, ceil(track / (i + 1)))
        
        return curMax
            
            
        
        