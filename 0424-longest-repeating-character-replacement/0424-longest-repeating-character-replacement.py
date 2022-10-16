class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AABABBA
        L   R  
        4-0+1=5
        5-3=2
        {A:3,B:2}
        MAX_=MAX(3,)
        """
        track=defaultdict(int)
        left,ans,max_=0,0,0
        
        for right in range(len(s)):
            
            track[s[right]] += 1

            max_=max(track[s[right]],max_)
            
            while (right-left+1) -max_>k:
                track[s[left]]-=1
                left+=1 
                
            ans = max(ans,right-left+1)
         
        return ans
                
            
        