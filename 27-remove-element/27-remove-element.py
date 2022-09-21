class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow,fast=0,1
        while slow<len(nums) and fast<len(nums):
            if nums[slow]==val and nums[fast]!=val:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
            elif nums[slow]!=val:
                slow+=1
            fast+=1
        if nums:    
            while nums and nums[-1]==val:
                nums.pop()
        