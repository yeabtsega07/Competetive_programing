class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def recur( index, track ):
            
            if index == -1 :
                if track == target: 
                    return 1
                return 0
            
            if (index, track - nums[index]) in dp :
                return dp[(index, track - nums[index])] 
            
            give = recur(index - 1, track + nums[index])
            notGive = recur(index - 1, track - nums[index])
            
            dp[(index, track - nums[index])] = give + notGive

            return dp[(index, track - nums[index])]
        
        
        ans = recur(len(nums) - 1, 0)

        return ans