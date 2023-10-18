class Solution:
    def calculate(self, s: str) -> int:
        opp="+"
        signs=["/","*","-","+"]
        nums=set(str(i) for i in range(10))
        stack=[]
        cur=0
        for i in range(len(s)):
            if s[i] in nums:
                cur= cur*10 + int(s[i])   
            if s[i] in signs or i==len(s)-1:
                if opp=="-":
                    stack.append(-cur)
                elif opp=="/":
                    stack[-1]=int(stack[-1]/cur)
                elif opp=="*":
                    stack[-1]*=cur
                else:
                    stack.append(cur)
                opp=s[i]
                cur=0  
                
        return sum(stack)        
      
                
                
                