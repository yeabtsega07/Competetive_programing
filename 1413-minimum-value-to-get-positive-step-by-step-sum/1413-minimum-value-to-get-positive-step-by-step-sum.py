class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre=[0]*len(nums)
        for i,num in enumerate(nums):
            if not pre: 
                pre[0]=num
            else:
                pre[i]=pre[i-1]+num
        ans=min(pre)
        return 1 if ans>=0 else -(ans-1)
                
                
        