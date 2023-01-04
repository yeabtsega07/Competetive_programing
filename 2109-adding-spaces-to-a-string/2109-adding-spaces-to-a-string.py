class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans, cur = [], []
        spaces = set(spaces)
        
        for i in range (len(s)):
            
            if i in spaces:
                ans.append("".join(cur))
                cur = []
            cur.append(s[i])
        
        if cur :
            ans.append("".join(cur))
            
        return " ".join(ans)
            
                
        