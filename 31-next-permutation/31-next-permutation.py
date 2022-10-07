class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        if len(nums)==1:
            return nums
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                break         
        j=len(nums)-1
        while j>i:
            if nums[j]>nums[i]:
                break
            j-=1 
        if j==i:
            return nums.reverse()
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i+1:])
                
    

        