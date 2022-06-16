class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        temp=[]
        for i in s:
            if i !=")":
                stack.append(i)
            else:
                
                check=stack.pop()
                while check!="(":
                    temp.append(check)
                    check=stack.pop()
                while temp:
                    stack.append(temp.pop(0))
        return "".join(stack)  
        