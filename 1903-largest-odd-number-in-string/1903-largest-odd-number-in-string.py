class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums = list(num)
        
        while nums and int(nums[-1]) % 2 == 0:
            nums.pop()
            
        
        return "".join(nums)