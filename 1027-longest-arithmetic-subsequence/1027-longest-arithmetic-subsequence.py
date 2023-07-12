class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        dp = {}
        
        for l in range(len(nums) - 1):
            
            for r in range(l + 1, len(nums)):
                
                diff =nums[r] - nums[l]
                dp[(r, diff )] = dp.get((l, diff), 1) + 1
        
        return max(dp.values())
                        
                        