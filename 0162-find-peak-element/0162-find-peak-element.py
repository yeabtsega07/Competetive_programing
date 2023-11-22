class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
            
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = left + (right - left) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        
        return left
        