class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        start=0
        end=1    
        while start<len(nums) and end < len(nums):
            if nums[start]==0 and nums[end]!=0:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
            elif nums[start]!=0:
                start+=1
            end+=1
         

            
                