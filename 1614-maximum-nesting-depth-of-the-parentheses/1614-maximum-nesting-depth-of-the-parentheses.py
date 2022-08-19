class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        cnt=0
        leng=0
        for i in s:
            if i=="(":
                cnt+=1
                stack.append(i)
            elif i==")":
                leng=max(cnt,leng)
                cnt-=1
                stack.pop()
        return leng        
                
        
        