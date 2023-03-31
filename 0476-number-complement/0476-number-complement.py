class Solution:
    def findComplement(self, num: int) -> int:
        
        for i in range(len(bin(num)[2:])):
            
            if num & ( 1 << i ) == 0:
                num |= (1 << i)
            else:
                num &= ~(1 << i)
                
        return num        
                
        