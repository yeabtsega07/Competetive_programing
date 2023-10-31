class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        cur = round(target / len(arr))
        
        less = 0
        for num in arr:
            if num <= cur:
                less += num
                
        def calc(val):
            res = 0
            for num in arr:
                if num <= val:
                    res += num
                else:
                    res += val
            return res
        
        low , high = cur, max(arr)
        while low < high:
            
            mid = low + (high - low) // 2
            if calc(mid) == target:
                return mid
            elif calc(mid) < target:
                low = mid + 1
            else:
                high = mid 
        

        if abs(calc(high - 1) - target) <= abs(calc(high) - target):
            return high - 1
        return high
            