class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l, res, curSum = 0, 0, 0
        
        for r in range(len(nums)):
            curSum += nums[r]
            
            while nums[r] * (r - l + 1) > curSum + k:
                curSum -= nums[l]
                l += 1
            
            res = max(res , r - l + 1)
        
        return res
                
        