class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        length = len(nums)
        nums = list(set(nums))
        nums.sort()
        
        result = float("inf")
        
        for i, num in enumerate(nums):
            
            index = bisect_right(nums, (num + (length - 1)))
            result = min(length - index + i, result)
        
        return result
        
        
        