class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        dp = {}
        
        def recur ( index, pre ):

            if index >= len(nums) - 1:
                return 1
            
            if  (index, pre) in dp:
                return dp[(index, pre)]
            
            take = 0
            if pre == float("inf") or (pre > 0 and nums[index + 1] - nums[index] < 0) or (pre < 0 and nums[index + 1] - nums[index] > 0):
                if nums[index] != nums[index + 1]: 
                    take += recur( index + 1, nums[index + 1] - nums[index] ) + 1
            
            notTake = recur(index + 1, pre)
            
            dp[(index, pre)] = max(take, notTake)
            return dp[(index, pre)]
        
        return recur(0, float("inf"))