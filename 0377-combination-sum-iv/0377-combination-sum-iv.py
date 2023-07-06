class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        
        def backtrack ( index, curSum ):
            
            if curSum >= target:
                return 1 if curSum == target else 0
            
            
            for i in range(len(nums)):
                
                if (i, curSum + nums[i]) in dp:
                    cur = dp[(i, curSum + nums[i])]
                else:    
                    cur = backtrack(i, curSum + nums[i])
                    
                dp[(index, curSum)] += cur
            
            return dp[(index, curSum)]
        
        res = 0
        for index, num in enumerate(nums):
            
            res += backtrack(index, num)
        
        return res
            
        