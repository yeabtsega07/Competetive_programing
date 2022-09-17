class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if len(nums)<firstLen+secondLen:
            return 0
        presum=[0]*len(nums)
        presum[0]=nums[0]
        for i in range(1,len(nums)):
            presum[i]=presum[i-1]+nums[i]
        maxFirst=presum[firstLen-1]
        maxSecond=presum[secondLen-1]
        ans=presum[firstLen+secondLen-1]
        for i in range(firstLen+secondLen,len(nums)): 
            maxFirst=max(maxFirst,presum[i-secondLen]-presum[i-secondLen-firstLen])
            maxSecond=max(maxSecond,presum[i-firstLen]-presum[i-secondLen-firstLen])
            ans=max(ans,maxFirst+presum[i]-presum[i-secondLen],maxSecond+presum[i]-presum[i-firstLen])
        return ans    
        

             
                    
                
                
            
            
        