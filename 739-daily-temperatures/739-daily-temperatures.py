class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack=[]
        check=[0]*len(temperatures)
        for i,j in enumerate (temperatures):
            while mono_stack and temperatures[mono_stack[-1]]<j:
                last=mono_stack.pop()
                check[last]=i-last
            mono_stack.append(i)
        return  check    
        
        