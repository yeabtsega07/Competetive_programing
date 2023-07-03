class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        s1 = list(s)
        s2 = list(goal)
        
        if s1 != s2 and len(s1) == len(s2):
            
            track = defaultdict(str)
            count = 0
            for i , val in enumerate(s1):
                
                if s1[i] != s2[i]:
                    count += 1

                    track[s1[i]] = s2[i]

                    
            
            if count > 2:

                return False

            if len(track) == 2 and set(track.values()) == set(track.keys()):
                return True
            
            return False
        
        elif s1 == s2:
            
            count = Counter(s1)
            if len(count) < len(s1):
                return True
            return False
        
        return False
                