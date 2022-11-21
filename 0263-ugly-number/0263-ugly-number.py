class Solution:
    def isUgly(self, n: int) -> bool:
        
        while n != 1:
            check = n
            
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
                
            if check == n:
                return False
        return True     