class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        res,pre=0,1
        slow,fast=0,0
        while fast<len(nums):
            pre*=nums[fast]
            while pre>=k:
                pre/=nums[slow]
                slow+=1
            res+=fast-slow+1
            fast+=1
        return res    
         
    