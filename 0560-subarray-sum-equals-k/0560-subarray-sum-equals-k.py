class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre={0:1}
        sum_,ans=0,0
        for i,n in enumerate(nums):
            sum_+=n
            if sum_-k in pre.keys():
                ans+=pre[sum_-k]
            if sum_ not in pre.keys():
                pre[sum_]=1
            else:
                pre[sum_]+=1        
        return ans        
            
                
                
            
        