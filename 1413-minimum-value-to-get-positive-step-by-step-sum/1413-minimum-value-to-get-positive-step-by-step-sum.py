class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum_=0
        minv=1
        for i,num in enumerate(nums):
            sum_+=num
            minv=min(minv,sum_)
        return minv if minv>=0 else -(minv-1)                
                
        