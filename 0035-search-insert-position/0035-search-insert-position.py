class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left, right = 0, len(nums) - 1
        return bisect_left(nums,  target)
#         while left <= right:
            
#             mid = left + (right - left) // 2
            
#             if  nums[ mid ] > target:
#                 right = mid - 1
#             elif  nums[ mid ] < target:
#                 left = mid + 1
#             else:
#                 return mid
        
        
#         return left
        
        
                