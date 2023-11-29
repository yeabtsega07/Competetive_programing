class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        
        for val in bin(n)[2:]:
            
            if val == "1":
                res += 1
        
        return res