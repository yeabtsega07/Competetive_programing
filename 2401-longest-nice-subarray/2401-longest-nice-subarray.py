class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        j=0
        max_=0
        num=0
        for i in range(0, len(nums)):
            while num & nums[i]:
                num^=nums[j]
                j+=1
            num|=nums[i]
            max_=max(max_,i-j+1)

        return max_      
                        
                    
        