class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        res = [0,float('inf')]
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for i , num in enumerate(nums):
            if i < len(nums) - 1: 
                cur  = (num // (i+1)) - ((nums[-1] - num) // (len(nums) - i - 1) )
            else:
                cur  = (num // (i+1)) - ((nums[-1] - num) // (len(nums) - i ) )
                
            if res[1] > abs(cur):
                res = [i, abs(cur)]
            
        return res[0]    
        