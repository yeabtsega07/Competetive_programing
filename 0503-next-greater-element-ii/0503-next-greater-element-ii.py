class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans, stack = [-1] * len(nums), []
        nums += nums 
        for i, num in enumerate(nums):
            
            while stack and nums[stack[-1]] < num:
                
                cur = stack.pop()
                ans[cur % len(ans)] = num
                
            stack.append(i)
        
        return ans
            
            
        