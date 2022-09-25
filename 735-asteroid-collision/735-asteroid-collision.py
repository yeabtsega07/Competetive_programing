class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            if not stack:
                stack.append(ast)
            else:
                if ast>0:
                        stack.append(ast)        
                while stack and stack[-1]>0 and ast<0 and -ast>stack[-1]:
                    stack.pop()
                if stack and stack[-1]==-ast:
                    stack.pop()
                elif not stack:
                    stack.append(ast)
                elif stack and stack[-1]<0 and ast<0:
                    stack.append(ast)
        return stack           