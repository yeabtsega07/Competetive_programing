class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sum_=sum(nums)
        n=len(nums)
        pre={}
        res=[]
        for i,num in enumerate(nums):
            if not pre:
                pre[i]=num
                continue
            pre[i]=pre[i-1]+num
        for i,num in enumerate(nums):
            if i==0 or i==n-1:
                res.append(abs(pre[n-1]-(n*num)))
            else:
                left=(i*num)-pre[i-1]
                right=pre[n-1]-(num*(n-1-i))-pre[i]
                res.append(left+right)           
        return res    
        