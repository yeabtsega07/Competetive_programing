class Solution:
    def prevPermOpt1(self, nums: List[int]) -> List[int]:
        
        check = nums[:]
        cur = -1
        for i in range(len(nums) - 1):
            
            if nums[i] > nums[i + 1]:
                cur = i
        if cur == -1:
            return nums
        
        check = len(nums) - 1
        while check >= cur - 1:
            if nums[check] < nums[cur] and nums[check] != nums[check - 1]:
                nums[cur], nums[check] = nums[check], nums[cur]
                return nums

            check -= 1
        return nums
            
        
        
                