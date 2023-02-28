class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack, path = [], path.split("/")
        
        for dir in path:
            
            if dir == "..":
                
                if  stack:
                    stack.pop()
            
            elif dir and dir != ".":
                stack.append(dir)
        
        return "/" + "/".join(stack)
            
            
                
        