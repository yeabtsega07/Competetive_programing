class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            
            if  char != "]":
                stack.append(char)
            else:
                cur = []
                
                while stack and stack[-1] != "[":
                    cur.append(stack.pop())
                
                stack.pop()
                
                num = []
                while stack and stack[-1].isnumeric():
                    num.append(stack.pop())
                
                cur = "".join(cur[::-1])
                num = int("".join(num[::-1]))
                
                stack.append(num*cur)
        
        return "".join(stack)