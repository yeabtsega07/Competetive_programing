class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start , end = 0,  0
        maxAverage, curSum = -float("inf"), 0
        
        
        while end < len(nums):
            
            curSum += nums[end]
            if end - start + 1 == k:
                curAvg = curSum / k 
                maxAverage = max(curAvg, maxAverage)
                curSum -= nums[start]
                start += 1
                
            
            end += 1   
        
        
        return maxAverage
                
                