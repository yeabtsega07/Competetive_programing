class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = defaultdict(int)
        
        for i in s1:
            check[i] += 1
        
        track = defaultdict(int)
        left = 0
        
        for right in range(len(s2)):
            track[s2[right]] += 1
            
            if right-left+1 == len(s1) and check == track:
                return True
            elif right-left+1 == len(s1):

                if track[s2[left]] > 1:
                    track[s2[left]] -= 1
                else:
                    track.pop(s2[left])
                left += 1
        return False if check != track else True        
                
        
        
        