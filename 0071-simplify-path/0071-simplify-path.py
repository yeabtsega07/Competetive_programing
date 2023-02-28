class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, cur = [] , []
        
        for i in range(len(path)):
            # print(cur, i, stack) 
            if path[i] == "/" and cur:
                if cur == ["/",".","."]:

                    if stack:
                        stack.pop()
                        cur = ["/"]
                    cur = ["/"]   
                elif cur == ["/","."]:
                    cur = ["/"]
                    
                else:
                    if len(cur) > 2 and cur[0] == cur[1] == "/":
                        stack.append("".join(cur[1:]))
                    elif cur == ["/"] :
                        cur = ["/"]
                    else:
                        stack.append("".join(cur))
                        
                    cur = ["/"]
                    
            else:
                
                cur.append(path[i])
        
        if cur == ["/",".","."]:
            if stack:
                stack.pop()
                cur = ["/"]
        elif cur and len(cur) > 1 and cur != ["/","."]:
            stack.append("".join(cur))
            
        return "".join(stack) if stack else "/"    
                
        