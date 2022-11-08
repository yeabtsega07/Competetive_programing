class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        
        for i in range(len(gain)):
            if i > 0:
                gain[i] += gain[i-1]
                
            res = max( res ,gain[i])
            
        return res   
        