class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        left, right = 0 , 0
        
        while left < len(nums1) and right < len(nums2):
            
            if nums1[left] <= nums2[right]:
                nums.append(nums1[left])
                left += 1
            else:
                nums.append(nums2[right])
                right += 1
        
        nums.extend(nums1[left :])
        nums.extend(nums2[right :])
        if len(nums) % 2:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2 