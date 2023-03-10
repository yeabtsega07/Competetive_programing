class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        
        def get_day ( weight ):
            
            day = 1
            curSum = 0
            
            for weight in weights:
                curSum += weight
                
                if curSum > mid:
                    day += 1
                    curSum = weight
            
            return day      
            
            
        low, high = max(weights) , sum(weights)

        while low < high :

            mid = low + (high - low) // 2

            if get_day(mid) > days:
                low = mid + 1

            else:
                high = mid
        
        return low

            
        
        
