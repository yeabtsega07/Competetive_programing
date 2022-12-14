class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(check):
            if check:
                pre, pre2 = nums[0], 0
        
                for i in range(1, len(nums)-1):
                    take = nums[i] + pre2
                    nonTake = 0 + pre
                    pre2 = pre
                    pre = max(take, nonTake)
        
                return pre
            else:
                pre, pre2 = nums[1], 0
        
                for i in range(2, len(nums)):
                    take = nums[i] + pre2
                    nonTake = 0 + pre
                    pre2 = pre
                    pre = max(take, nonTake)
        
                return pre
        if len(nums) == 1:
            return nums[0]
        return max(helper(1), helper(0))
                
            
        