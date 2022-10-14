class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        nums.sort()
    
        res=[]
        for i,n in enumerate(nums):
            if i==0 and nums[i+1]!=n+1 and nums[i+1]!=n:
                res.append(n)
            elif i==len(nums)-1 and nums[i-1]!=n-1 and nums[i-1]!=n:
                res.append(n)
            elif 0<i<len(nums)-1 and nums[i+1]!=n+1 and nums[i+1]!=n and nums[i-1]!=n-1 and nums[i-1]!=n:
                res.append(n)
        
        return res
    
                
                
        