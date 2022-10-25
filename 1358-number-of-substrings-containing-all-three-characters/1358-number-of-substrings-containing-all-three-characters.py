class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        track = defaultdict(list)
        left = 0
        ans = 0
        for  i,char in enumerate(s) :
            track[char].append(i)
        
        while track["a"] and track["c"] and track["b"]:
            if s[left] == "a":
                last = max(track["b"][0],track["c"][0])
                track["a"].pop(0)
            elif s[left] == "b":
                last = max(track["a"][0],track["c"][0])
                track["b"].pop(0)
            else:
                last = max(track["a"][0],track["b"][0])
                track["c"].pop(0) 
            ans += (len(s)-last) 
            left += 1
        return ans         
        