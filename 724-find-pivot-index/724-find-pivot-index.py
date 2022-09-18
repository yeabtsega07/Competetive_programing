class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n=len(nums)-1
        pre=[0]*(n+1)
        suf=[0]*(n+1)
        for i in range(1,n+1):
            pre[i]=pre[i-1]+nums[i-1]
            suf[n-i]=suf[n-i+1]+nums[n-i+1]
        for i in range(n+1):
            if pre[i]==suf[i]:
                return i
        return -1    
            


  
        