class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        track = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        for i, char in enumerate(pattern):
            if char in track:
                if track[char] != s[i]:
                    return False
            else:
                track[char] = s[i]
                
        if len(track.keys()) != len(set(track.values())): 
            return False
        return True
        