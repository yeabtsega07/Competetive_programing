class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        curMin = len(s) + 1
        check = Counter(t)

        
        def is_valid( check, track ):
            
            for key in check:
                
                if check[key] > track[key]:
                    return False
            
            return True    
        
        track, left = defaultdict(int), 0
        minL, minR = float("inf"), float("inf")
        
        for right, char in enumerate(s):
            

            track[char] += 1

            while is_valid( check , track ) and left <= right:
                
                if right - left + 1 < curMin: 
                    minR , minL = right, left
                    curMin = right - left + 1
                    
                track[s[left]] -= 1
                
                if not track[s[left]]:
                    track.pop(s[left])
                
                left += 1
            
        return s[minL : minR + 1] if minL != float("inf")  and minR != float("inf") else ""
            