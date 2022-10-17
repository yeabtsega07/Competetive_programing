class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start, end = float("inf"), 0
        
        for i,num in enumerate(nums):
            
            while stack and nums[stack[-1]] > num:
                start =  min(stack.pop(), start)
            
            stack.append(i)
        
        stack.clear()
        
        for i in range (len(nums)-1,-1,-1):
            
            while stack and nums[stack[-1]] < nums[i]:
                end =  max(stack.pop(), end)
            
            stack.append(i)
            
       
        return end-start+1 if start< end else 0        