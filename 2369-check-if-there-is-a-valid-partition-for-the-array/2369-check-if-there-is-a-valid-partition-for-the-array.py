class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        dp = {}
        
        def recur( index ):
            
            if index in dp:
                return dp[index]
            
            if index >= len(nums):
                return True
            
            if len(nums) - index < 2:
                return False
            
            choice1 = False
            if nums[index] == nums[index + 1]:
                choice1 = recur(index + 2)
            
            choice2 = False
            if index + 3 <= len(nums) and nums[index] == nums[index + 1] == nums[index + 2]:
                choice2 = recur(index + 3)
            
            choice3 = False
            if index + 3 <= len(nums) and nums[index] + 2 == nums[index + 1] + 1 == nums[index + 2]:
                choice3 = recur(index + 3)
            

            dp[index] = choice1 or choice2 or choice3
            return dp[index]
        
        return recur(0)
        