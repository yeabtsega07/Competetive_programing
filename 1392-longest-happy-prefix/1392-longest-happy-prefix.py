class Solution:
    def longestPrefix(self, s: str) -> str:
        
        
            m = len(s)
            prevLPS, i = 0, 1
            LPS = [0 for _ in range(m)]
            while i < m:
                if s[prevLPS] == s[i]:
                    LPS[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1
                else:
                    if prevLPS == 0:
                        i += 1
                    else:
                        prevLPS = LPS[prevLPS - 1]
            return s[0 : LPS[-1]]
            
            
        