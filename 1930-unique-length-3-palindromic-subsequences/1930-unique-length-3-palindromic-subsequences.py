class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        h = defaultdict(list)
        ans = 0
        
        for idx in range(len(s)):
            h[s[idx]].append(idx)
            
        for k,v in h.items():
            if len(v) >= 2:
                ans += len(set(s[v[0]+1:v[-1]]))

        return ans
            
        