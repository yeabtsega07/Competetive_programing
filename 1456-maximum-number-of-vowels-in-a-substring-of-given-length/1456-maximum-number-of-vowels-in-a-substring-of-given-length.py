class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        slow,fast=0,0
        check="aeiou"
        res=0
        cnt=0
        while fast<len(s):
            if s[fast] in check:
                cnt+=1
            if fast-slow+1==k:
                res=max(res,cnt)
                if s[slow] in check:
                    cnt-=1
                slow+=1    
            fast+=1
        return res     
            
        