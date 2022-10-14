class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,n in enumerate(nums):
            nums[i]*=n
        return sorted(nums)    

        
        