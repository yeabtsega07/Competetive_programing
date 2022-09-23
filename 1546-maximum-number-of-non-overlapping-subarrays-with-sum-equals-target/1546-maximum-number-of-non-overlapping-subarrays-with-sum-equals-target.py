class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre={0:-1}
        ans=0
        lastIdx=-1
        sum_=0
        for i , num in enumerate(nums):
            sum_+=num
            find=sum_-target
            if find in pre.keys() and pre[find]>=lastIdx:
                ans+=1
                lastIdx=i
            pre[sum_]=i    
        return ans       
                
                    
                    
        