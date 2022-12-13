class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, pre2 = nums[0], 0
        
        for i in range(1, len(nums)):
            
            take = nums[i]  + pre2
            
            nonTake = 0 + pre
            
            cur = max(take, nonTake)
            pre2 = pre
            pre = cur
        
        return pre
             
        