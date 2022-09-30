class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem={0:1}
        ans,sum_=0,0
        for num in nums:
            sum_+=num
            if sum_%k not in rem.keys():
                rem[sum_%k]=1
            else:
                ans+=rem[sum_%k]
                rem[sum_%k]+=1 
        return ans       
                   
            