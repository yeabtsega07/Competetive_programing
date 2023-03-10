class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def get_threshold( divider ):
            
            curSum = 0
            for num in nums:
                curSum += ceil(num / divider)
            
            return curSum
        
        low, high = 1, max(nums)
        
        while low <= high:
            
            mid = low + (high - low) // 2
            
            if get_threshold(mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        
        return high + 1