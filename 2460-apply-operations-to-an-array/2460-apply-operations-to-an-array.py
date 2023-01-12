class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        """
        122110
        140200
        """
        for i in range(len(nums) - 1):
            
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            else:
                nums[i] = nums[i]
        
        left = 0
        right = 1
        while left < len(nums) and right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1
            right += 1
        
        return nums 
        