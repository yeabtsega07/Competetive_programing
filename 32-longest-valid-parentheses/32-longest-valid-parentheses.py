class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leng=0
        stack=[-1]
        for i ,char in enumerate(s):
            if char=="(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    leng=max(leng,i-stack[-1])
                else:
                    stack.append(i)
        return leng         
            
                

                
            