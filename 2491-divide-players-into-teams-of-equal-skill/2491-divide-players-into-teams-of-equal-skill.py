class Solution:
    def dividePlayers(self, nums: List[int]) -> int:
        nums.sort()
        
        left, right = 0, len(nums) - 1
        ans, check = 0, nums[left] + nums[right]
        
        while left < right:
            
            if nums[left] + nums[right] == check:
                ans += (nums[left] * nums[right])
            
            else:
                return -1
            
            left += 1
            right -= 1
        
        return ans