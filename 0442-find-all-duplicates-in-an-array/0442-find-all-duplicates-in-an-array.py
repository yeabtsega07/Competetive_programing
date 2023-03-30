class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []
        i = 0
        while i < len(nums):
            
            if nums[i] != nums[nums[i] - 1]:
                j = nums[i]
                nums[i] , nums[j - 1] = nums[j - 1], nums[i] 
            else:
                i += 1
        
        
        for i, num in enumerate(nums):
            
            if num != i + 1:
                result.append(num)
        
        return result
        