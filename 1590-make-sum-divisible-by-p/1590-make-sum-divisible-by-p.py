class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem=0
        minlen=len(nums)
        for num in nums:
            rem=(num+rem)%p
            
        if rem==0:
            return 0
        
        pre=0
        dic={0:-1}
        for i,num in enumerate(nums):
            pre=(pre+num)%p
            key=(pre+p-rem)%p
            if key in dic.keys():
                minlen=min(minlen,i-dic[key])
            dic[pre]=i
        return minlen if minlen!=len(nums) else -1    

        