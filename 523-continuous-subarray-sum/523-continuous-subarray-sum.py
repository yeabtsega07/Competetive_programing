class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem={0:-1}
        pre=0
        for i,n in enumerate(nums):
            pre+=n
            if pre%k not in rem:
                rem[pre%k]=i
            elif i- rem[pre%k]>1:
                return True
        return False    
        