class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/" :
                num1=stack.pop()
                num2=stack.pop()
                if i == "+":
                    stack.append(num2+num1)
                elif i == "-":
                    stack.append(num2-num1)     
                elif i == "*":
                    stack.append(num2*num1)    
                elif i == "/":
                    stack.append(int(num2/num1))    
            else:
                stack.append(int(i))
        return stack[-1]      
                
        