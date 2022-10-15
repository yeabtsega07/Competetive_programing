class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        track=set()
        cur=""
        ans=set()
        fast=0
        while fast<len(s)-9:
            cur=s[fast:fast+10]
            if len(cur)==10 and cur in track:
                ans.add(cur)
            track.add(cur)
            fast+=1    
        return list(ans)   
        