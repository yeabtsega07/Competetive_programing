class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        sum_=0
        ans=0
        for i,num in enumerate(nums):
            sum_+=num
            if sum_-k in prefix.keys():
                ans+=prefix[sum_-k]     

            if sum_ in prefix.keys():
                    prefix[sum_]+=1
            else:    
                     prefix[sum_]=1
        return ans                
                
                
                
            
        