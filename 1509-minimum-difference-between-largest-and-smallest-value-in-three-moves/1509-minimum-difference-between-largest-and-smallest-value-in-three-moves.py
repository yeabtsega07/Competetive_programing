class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3: return 0
        return min(nums[len(nums)-1]-nums[3],nums[len(nums)-2]-nums[2],nums[len(nums)-3]-nums[1],nums[len(nums)-4]-nums[0])
        