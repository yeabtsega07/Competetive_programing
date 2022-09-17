class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        sum_=0
        ans=0
        for num in nums:
            sum_+=num
            ans+=prefix.get(sum_-k,0)
            prefix[sum_]=1+prefix.get(sum_,0)
        return ans                
                
                
                
            
        