class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = nums[i] + nums[j]
                index = bisect_left(nums, target)

                
                if index < len(nums) and nums[index] != nums[j]:
                    count += (index - 1) - j
                elif index >= len(nums) :
                        count += (len(nums) - 1) - j

        
        return count
                
        