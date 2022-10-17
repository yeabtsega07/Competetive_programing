class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numSorted = sorted(nums)
        start, end = float("inf"), 0
        
        for i,num in enumerate(nums):
            if numSorted[i] != num:
                start = min(start,i)
                end = max(end,i)
                
        return end-start+1 if start< end else 0        