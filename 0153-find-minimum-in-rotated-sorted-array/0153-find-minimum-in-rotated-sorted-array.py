class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def get_pivot(nums):
            left, right = 0, len(nums) - 1

            while left < right:

                mid = left + (right - left) // 2

                if  nums[mid] > nums[mid + 1]:
                    return mid
                if  nums[mid] < nums[mid - 1]:
                    return mid - 1

                if nums[left] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return left
        
        index = get_pivot(nums)

        if index == len(nums) - 1:
            return nums[0]
        else:
            return nums[index + 1]