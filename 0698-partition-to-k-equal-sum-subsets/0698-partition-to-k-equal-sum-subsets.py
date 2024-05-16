class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k != 0:
            return False
        value = summ//k
        @cache
        def dp(bitmask, target):
            if target < 0:
                return False
            
            if bitmask+1 == 2**len(nums):
                return target == 0
            
            if target == 0:
                target = value
                
            ans = False
            for i in range(len(nums)):
                if bitmask & (1 << i) == 0:
                    bitmask ^= (1<<i)
                    ans = ans or dp(bitmask,target-nums[i])
                    bitmask ^= (1<<i)
            return ans

        return dp(0,value)