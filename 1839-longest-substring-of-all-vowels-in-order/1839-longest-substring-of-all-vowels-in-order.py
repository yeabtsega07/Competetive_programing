class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(word) < 5:
            return 0
        count = 1
        cur, res = 1,1
        
        for right, char in enumerate(word):
            if right == 0 :
                continue
                
            if word[right-1] <= char:
                if word[right-1] != char:
                    count += 1
                cur += 1    
            else:
                
                if count == 5:
                    res = max (cur , res)
                cur = 1
                count = 1
        if count == 5:
            res = max (cur , res)
        return res if res >= 5 else 0             
        