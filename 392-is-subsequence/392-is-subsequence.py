class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str1,str2=0,0
        while str1<len(s) and str2<len(t):
            if s[str1]==t[str2]:
                str1+=1
            str2+=1
        return str1==len(s)    
                