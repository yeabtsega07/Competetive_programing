class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict = {}
        for i in range(1, 27):
            
            dict[str(i)] = chr(i + 96)
        
        if len(s) < 3:
            return dict[s[0]] + dict[s[1]]
        
        ans, cur = "", s[0]    
        for i in range(1, len(s) - 1):
            if s[i] != "#":
                cur += s[i]
            if s[i + 1] == "#":
                ans += dict[cur]
                cur = ""
                continue
            if len(cur) == 2:    
                ans += dict[cur[0]]
                cur = cur[1]
                
        if cur :
            ans += dict[cur]
        if s[-1] != "#":
            ans += dict[s[-1]]
        return ans     
             
                
                
            
            