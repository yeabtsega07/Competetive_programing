class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track={}
        left=0
        ans=0
        
        for right in range(len(s)):
            
            track[s[right]] = 1+track.get(s[right],0)
            
            while sum(track.values())-max(track.values())>k:
                if track[s[left]]>1:
                    track[s[left]]-=1
                else:
                    track.pop(s[left])
                left+=1    
            ans = max(ans,right-left+1)
         
        return ans
                
            
        