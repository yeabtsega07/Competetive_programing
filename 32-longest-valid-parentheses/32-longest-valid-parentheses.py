class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leng=0
        lft,rgt=0,0
        for i in range(len(s)-1):
            if s[i]=="(" :
                lft+=1
            elif s[i]==")":
                rgt+=1
            if lft==rgt:
                leng=max(leng,(lft+rgt))
            elif rgt>=lft:
                lft,rgt=0,0    
        lft,rgt=0,0 
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                lft+=1
            elif s[i]==")":
                rgt+=1 
            if lft==rgt:
                leng=max(leng,(lft+rgt))
            elif lft>=rgt:
                lft,rgt=0,0    
        return leng         
            
                

                
            