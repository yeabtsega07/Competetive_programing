class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre, l = 0, 0
        res = float("inf")
        
        for r in range(len(nums)):
            pre += nums[r]
            
            while pre >= target:
                res = min(res, r - l + 1 )
                pre -= nums[l]
                l += 1
            
        return res if res != float("inf") else 0    
                