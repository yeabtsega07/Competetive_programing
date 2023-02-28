class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if  n == 1.0:
            return True
        
        elif n % 4 != 0 or n < 1:
            return False
        
        return self.isPowerOfFour(n / 4)
"""
josii going to places 
"""
