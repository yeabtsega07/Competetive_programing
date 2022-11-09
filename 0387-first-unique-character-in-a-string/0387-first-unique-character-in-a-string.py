class Solution:
    def firstUniqChar(self, s: str) -> int:
        track = Counter(s)
        
        for i in range(len(s)):
             if track[s[i]] == 1:
                    return i
        
        return -1
        