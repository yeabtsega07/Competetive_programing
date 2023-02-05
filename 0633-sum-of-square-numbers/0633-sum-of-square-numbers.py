class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range( int(sqrt(c)) + 1)]
        
        left, right = 0, len(nums) - 1
        # print(nums)
        while left <= right:
            
            if nums[left] ** 2 + nums[right] ** 2 == c :
                return True
            elif nums[left] ** 2 + nums[right] ** 2 > c:
                right -= 1
            else:
                left += 1
        
        return False
        