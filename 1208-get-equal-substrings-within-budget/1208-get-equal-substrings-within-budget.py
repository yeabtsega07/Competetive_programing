class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curSum, left, ans = 0, 0 ,0
        
        for right,char in enumerate(s):
            
            curSum += abs(ord(char)  - ord(t[right]))
            
            while curSum > maxCost:
                
                curSum -= abs(ord(s[left])  - ord(t[left]))
                left += 1
            
            ans = max(ans, right-left+1)
            
        return ans    
            
        