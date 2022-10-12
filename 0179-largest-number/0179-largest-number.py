class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
        
        for i  in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
                
        return str(int("".join(nums)))       
                    
        
        