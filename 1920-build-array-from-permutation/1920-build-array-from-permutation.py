class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums = [(num , -1) for num in nums]

        for i, num in enumerate(nums):
            nums[i] = (num[0] , nums[num[0]][0])
        # print(nums)
        nums = [num[1] for num in nums]
        return nums  
        
        