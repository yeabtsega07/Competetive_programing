class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def recur(ind):
            if ind == 0:
                return nums[ind]
            if ind < 0:
                return 0
            pick = nums[ind] + recur(ind-2)
            nonPick = 0 + recur(ind-1)
            return max(pick, nonPick)
    
        return recur(len(nums) -  1)
            
        