class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans, j = [], 0
        
        for i in range (len(s)):
            if j < len(spaces) and i == spaces[j]:
                ans.append(" ")
                j += 1
            ans.append(s[i])
            
        return "".join(ans)
            
                
        