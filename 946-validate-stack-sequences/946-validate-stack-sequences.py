class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        point=0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while len(stack) and point<len(popped)and popped[point]==stack[-1]:
                stack.pop()
                point+=1
        if not stack:
            return True