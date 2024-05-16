class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k != 0:
            return False
        value = summ//k
        @cache
        def dp(bitmask,k,target):
            if target < 0:
                return False
            if target == 0:
                k -= 1
                target = value
            if k == 0:
                return bitmask+1 == 2**len(nums)
            
            ans = False
            for i in range(len(nums)):
                if bitmask & (1 << i) == 0:
                    bitmask ^= (1<<i)
                    ans = ans or dp(bitmask,k,target-nums[i])
                    bitmask ^= (1<<i)
            return ans

        return dp(0,k,value)