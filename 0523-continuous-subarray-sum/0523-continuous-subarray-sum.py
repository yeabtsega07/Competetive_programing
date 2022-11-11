class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0:-1}
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            
            if curSum % k in rem.keys():
                if i - rem[curSum % k] >= 2:
                    return True
            else:
                rem[curSum % k] = i
        
        return False
        