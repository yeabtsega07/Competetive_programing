class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem={}
        sum_=0
        for num in nums:
            sum_+=num
            if sum_%k not in rem.keys():
                rem[sum_%k]=1
            else:
                rem[sum_%k]+=1
        ans=0 
        if 0 in rem.keys():
            ans+=sum(range(0,rem[0]+1))
            rem[0]=1
        for i in rem.values():
            ans+=sum(range(0,i))
        return ans    
            
                   
            