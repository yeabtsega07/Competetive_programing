class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i,num in enumerate(nums):
            if num%2:
                nums[i]=1
            else:
                nums[i]=0
        sum_=0
        ans=0
        prefix={0:1}
        for num in nums:
            sum_+=num
            ans+=prefix.get(sum_-k,0)
            prefix[sum_]=1+prefix.get(sum_,0)
        return ans
        

                    
                    
                    