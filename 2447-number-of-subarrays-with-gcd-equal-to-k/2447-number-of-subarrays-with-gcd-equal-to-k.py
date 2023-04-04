class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd ( num1, num2):
            
            if not num2:
                return num1
            
            return gcd( num2, num1 % num2 )
        
        result = 0
        
        for i in range( len(nums) ):
            
            factor  = nums[i]
            
            for j in range (i , len(nums)):
                
                factor = gcd(factor, nums[j])
                
                if factor == k :
                    result += 1
        
        return result
        
        