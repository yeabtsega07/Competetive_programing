class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        l, r = 1 , x // 2
        ans = 1
        while l <= r:
            
            mid = l + ( r - l) // 2
            
            if mid ** 2 > x:
                r = mid - 1
                
            else:
                l = mid + 1
                ans = mid
                
        return ans
        