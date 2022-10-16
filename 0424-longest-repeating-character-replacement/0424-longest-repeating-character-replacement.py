class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        track={}
        left=0
        ans=0
        sum_,max_=0,0
        for right in range(len(s)):
            
            track[s[right]] = 1+track.get(s[right],0)
            sum_+=1
            max_=max(track[s[right]],max_)
            
            while sum_-max_>k:
                if track[s[left]]>1:
                    track[s[left]]-=1
                else:
                    track.pop(s[left])
                sum_-=1
                left+=1    
            ans = max(ans,right-left+1)
         
        return ans
                
            
        