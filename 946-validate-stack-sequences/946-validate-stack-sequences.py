class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        point=0
        for i in (pushed):
            stack.append(i)
            while len(stack) and popped[point]==stack[-1]:
                stack.pop()
                point+=1
        return point==len(popped)