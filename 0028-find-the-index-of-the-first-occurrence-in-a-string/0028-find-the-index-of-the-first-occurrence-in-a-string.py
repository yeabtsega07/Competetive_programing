class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        needle = list(needle)
        k,l = len(needle),0
        res,cur = float("inf"),defaultdict(int)
        
        for r in range(len(haystack)):
            
            if len(cur) == k:
                
                if list(cur.values()) == needle:
                    res = min(res ,l)
                l += 1
                cur.pop(l-1) 
            
            cur[r] = haystack[r]
        
        if list(cur.values()) == needle:
                    res = min(res ,l)
        return res if res != float("inf") else -1