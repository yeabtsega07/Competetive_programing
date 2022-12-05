class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        res = [0,float('inf')]
        preSum, totalSum = 0, sum(nums)
        
        for i , num in enumerate(nums):
            preSum += num
            
            if i < len(nums) - 1: 
                cur  = (preSum // (i+1)) - ((totalSum - preSum) // (len(nums) - i - 1) )
            else:
                cur  = (preSum // (i+1)) - ((totalSum - preSum) // (len(nums) - i ) )
                
            if res[1] > abs(cur):
                res = [i, abs(cur)]
            
        return res[0]    
        