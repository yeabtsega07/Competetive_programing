class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd( num1, num2):
            
            if not num2:
                return num1
            
            return gcd( num2, num1 % num2 )
        
        return gcd ( max(nums), min(nums) )
        