class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
        if n%2:
            return False
        for i in s:
            if i=="(":
                stack.append(i)
            elif i=="[":
                stack.append(i)
            elif i=="{":
                stack.append(i)
            elif i==")":
                if len(stack)!=0:
                    if stack[-1] =="(":
                        stack.pop()
                    else: 
                        return False
                else:
                    return False
            elif i=="]":
                if len(stack)!=0:
                    if stack[-1] =="[":
                        stack.pop()
                    else: 
                        return False
                else:
                    return False    
            elif i=="}":
                if len(stack)!=0:
                    if stack[-1] =="{":
                        stack.pop()    
                    else: 
                        return False
                        
                else:
                    return False      
                    
        if len(stack)==0:
            return True
        return False