class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        lSum = 0
        sum_ = sum(nums)
        for i, n in enumerate(nums):
            sum_ -= n
            if lSum == sum_:
                return i
            else:
                lSum += n
            if lSum == 0 and i == len(nums):
                return i
            if sum_ == 0 and i == 0:
                return 0
        return -1     
                
            
            
        