class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [num for num in str(n)]
        
        if len(nums) == 1:
            return -1
        
        for i in range(len(nums) - 2, -1 , -1):
            
            if nums[i + 1] > nums[i]:
                break
        
        left, right = i, len(nums) - 1
        
        while right > left:
            
            if nums[right] > nums[left]:
                break
            right -= 1
        
        if right == left:
            return -1
        
        nums[right], nums[left] = nums[left], nums[right]
        nums[left + 1:] = nums[left + 1:][::-1]
        
        return int("".join(nums)) if int("".join(nums)) <= 2 ** 31 - 1 else -1
        
        