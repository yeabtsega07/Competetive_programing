class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i,num in enumerate(nums):
            if i==0:
                pass
            else:
                nums[i]=num+nums[i-1]
        return nums       
            