class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        first, second = 0, 1
        ans = 0
        nums.sort(reverse = True)
        for third in range(2, len(nums)):
            if nums[first] + nums[second] > nums[third] and nums[second] + nums[third] > nums[first] and nums[first] + nums[third] > nums[second]:
                ans = max(nums[first] + nums[second] + nums[third], ans)
            
            first = second
            second = third
        
        return ans     
                
        