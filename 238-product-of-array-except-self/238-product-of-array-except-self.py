class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        pre[0]=nums[0]
        suf[len(nums)-1]=nums[len(nums)-1]
        n=len(nums)-1
        ans=[1]*len(nums)
        for i, num in enumerate(nums):
            if i ==0:
                continue
            pre[i]=pre[i-1]*num
            suf[n-i]=suf[n-i+1]*nums[n-i]
        for i in range(len(nums)):
            if i==0:
                ans[i]=suf[i+1]
            elif i==len(nums)-1:
                ans[i]=pre[i-1]
            else:
                ans[i]=pre[i-1]*suf[i+1]
        return ans        
                
                
            
            
        