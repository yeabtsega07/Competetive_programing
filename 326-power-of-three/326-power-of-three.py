class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        elif n==1.0:
            return True
        else: 
            return self.isPowerOfThree(n/3)
        