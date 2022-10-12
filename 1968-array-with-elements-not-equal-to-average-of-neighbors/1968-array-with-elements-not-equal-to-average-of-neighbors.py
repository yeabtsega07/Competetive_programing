class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        n=ceil(len(nums)/2)
        l,r=0,n
        while l<n and r<len(nums):
            
            ans.append(nums[l])
            ans.append(nums[r])
            l+=1
            r+=1
        if l<n:
            ans.append(nums[l])
        return ans    
            
            
        
        