class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        pre=-1
        moves=0
        for i in range(len(nums)):
            if nums[i]<=pre:
                moves+=pre-nums[i]+1
                nums[i]+=pre-nums[i]+1
            pre=nums[i]    
        return moves        
        