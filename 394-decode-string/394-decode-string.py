class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in s:
            if i !="]":
                stack.append(i)   
            else:
                char=""
                while stack[-1]!="[":
                    char=stack.pop()+char  
                stack.pop()    
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num    
                stack.append(int(num)*char)    
                    
        return "".join(stack)
                    
                    
                    
        