class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        check=[]
        res=0
        lft,right=0,0
        while right<len(s):  
            if s[right] in check:
                while s[right] in check:
                    check.pop(0)
            check.append(s[right])
            if len(check)>=3:
                res+=1
                check.pop(0)
            right+=1
        return res    
                
        