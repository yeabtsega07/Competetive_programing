class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            n = abs(n)
            if nums[n] < 0:
                return n
            nums[n] = -nums[n]
            
#         for i in range(len(nums)):
#             nums[i] = abs(nums[i])
        
#         return dup
            
            
        
        
        