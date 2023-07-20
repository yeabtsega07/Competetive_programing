class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        
        stack = [ ]
        
        for i, size in enumerate(asteroids):

            inserted = 1
            while stack and (stack[-1] > 0 and size < 0):

                cur = stack.pop()
                if abs(cur) > abs(size):
                    stack.append(cur)
                    inserted = 0
                    break
                elif  abs(cur) == abs(size) :
                    inserted = 0
                    break
            
            if inserted:

                stack.append(size)
        
        return stack