class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        pre={0:0}
        sum_=0
        for i , n in enumerate(nums):
            sum_+=n
            if sum_%k not in pre:
                pre[sum_%k]=i+1
            elif pre[sum_%k]<i:
                return True
        return False    
            
            
        