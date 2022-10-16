class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        track=defaultdict(int)
        left,ans,max_=0,0,0
        
        for right in range(len(s)):
            
            track[s[right]] += 1

            max_= max(track[s[right]],max_)
            
            while (right-left+1) -max_>k:
                track[s[left]] -= 1
                left+=1 
                
            ans = max(ans,right-left+1)
            
        return ans
                
            
        