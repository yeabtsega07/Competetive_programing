class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        opps=["*","+","-","/"]
        for i, tok in enumerate(tokens):
            if tok in opps:
                a=stack.pop()
                b=stack.pop()
                if tok=="*":
                    stack.append(a*b)
                elif tok=="+":
                    stack.append(a+b)
                elif tok=="/":
                    if b/a <0:
                        stack.append(ceil(b/a))
                    else:
                        stack.append(b//a)
                elif tok=="-":
                    stack.append(b-a)   
            else:
                stack.append(int(tok))   
        return stack[0]        
                    
        