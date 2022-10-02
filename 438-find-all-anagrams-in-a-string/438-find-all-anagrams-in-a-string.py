class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        sdi={}
        pdi={}
        for i in range(len(p)):
            sdi[s[i]]=sdi.get(s[i],0)+1
            pdi[p[i]]=pdi.get(p[i],0)+1
        ans=[0] if sdi==pdi else []
        slow=0
        for fast in range(len(p),len(s)):
            sdi[s[fast]]=sdi.get(s[fast],0)+1
            sdi[s[slow]]-=1
            if sdi[s[slow]]==0:
                sdi.pop(s[slow])
            slow+=1
            if sdi==pdi:
                ans.append(slow)
        return ans        
                    
            

                
        