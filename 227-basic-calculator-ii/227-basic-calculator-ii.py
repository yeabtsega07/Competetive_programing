class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        cur_num=0
        sign="+"
        nums=set(str(x) for x in range(10))
        opps={"+","-","/","*"}
        for i in range(len(s)):
            char=s[i]
            if char in nums:
                cur_num=cur_num*10+int(char)
            if char in opps or i==len(s)-1:
                
                if sign=="/" and stack:
                    stack[-1]=int(stack[-1]/cur_num)
                elif sign=="*" and stack:
                    stack[-1]*=cur_num
                elif sign=="-" and stack:
                    stack.append(-cur_num)
                else:
                    stack.append(cur_num)
                sign=char
                cur_num=0
        return sum(stack)       
                
                
                