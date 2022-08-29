class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        if len(nums)<=2:
            return nums.reverse()
        pt1=len(nums)-2
        pt2=len(nums)-1
        while pt1>=0:
            if nums[pt1]>=nums[pt2]:
                pt1-=1
                pt2-=1
            else:
                break
        if pt1==-1:
            return nums.reverse()
        for i in reversed(range(len(nums))):
            if nums[i]>nums[pt1]:
                nums[pt1],nums[i]=nums[i],nums[pt1]
                break
        nums[pt1+1:] = reversed(nums[pt1+1:]) 
        