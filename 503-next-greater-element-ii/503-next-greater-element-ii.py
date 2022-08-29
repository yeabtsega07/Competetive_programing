class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        mon_stack=[]
        for i in reversed(range(len(nums))):
            while mon_stack and nums[i]>=mon_stack[-1]:
                mon_stack.pop()
            if mon_stack and nums[i]<mon_stack[-1]:
                ans[i]=mon_stack[-1]
            mon_stack.append(nums[i]) 
            
        for i in reversed(range(len(nums))):
            while mon_stack and nums[i]>=mon_stack[-1]:
                mon_stack.pop()
            if mon_stack and nums[i]<mon_stack[-1]:
                ans[i]=mon_stack[-1]
            mon_stack.append(nums[i])     
            
        return ans    
                
                
        
