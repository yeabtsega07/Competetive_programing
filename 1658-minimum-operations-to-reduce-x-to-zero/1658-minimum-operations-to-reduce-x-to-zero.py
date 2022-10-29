class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        res,preSum = -1, 0
        left = 0
        goal = sum(nums) - x
        for right,n in enumerate(nums):
            preSum += n
            
            while preSum > goal and left<=right:
                preSum -= nums[left]
                left += 1
            if preSum == goal:
                    res = max(res, right-left+1)
                    
        return len(nums) - res if res != -1 else -1        
            
