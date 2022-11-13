class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        ans = ""
        
        for i,word in enumerate(reversed(temp)):
            
            ans += word
            if i != len(temp)-1:
                ans += " "
        
        return ans
            
        