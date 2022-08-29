class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        mon_stack=[]
        for i in range(len(temperatures)):
            while mon_stack and temperatures[i]>temperatures[mon_stack[-1]]:
                val=mon_stack.pop()
                ans[val]=i-val
            mon_stack.append(i)
        return ans
