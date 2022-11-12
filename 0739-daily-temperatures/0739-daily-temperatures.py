class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        track = {}
        stack = []
        
        for i, num in enumerate(temperatures):
            
            
            while stack and temperatures[stack[-1]] < num:
                val = stack.pop()
                track[val] = i - val
            
            if not stack:
                count = 0
            
            stack.append(i)
        
        ans = []
        for i,num in enumerate(temperatures):
            
            if i in track.keys():
                ans.append(track[i])
            else:
                ans.append(0)
        
        return ans
            