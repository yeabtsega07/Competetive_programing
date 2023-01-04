class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        s = s.split(" ")
        maxLenght = max(s, key = lambda p : len(p))
        
        for i in range(len(maxLenght)):
            
            cur = []
            for j in range(len(s)):
                
                if i < len(s[j]):
                    cur.append(s[j][i])
                else:
                    cur.append(" ")
            
            for x in range(len(cur) - 1, -1,  -1):
                if cur[x] == " ":
                    cur.pop()
                else:
                    break
                    
            ans.append("".join(cur))
                    
        return ans
        