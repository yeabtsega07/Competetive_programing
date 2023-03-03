class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 1 , x // 2

        while l < r:
            
            mid = l + ( r - l) // 2
            
            if mid ** 2 > x:
                r = mid - 1
                
            else:
                l = mid + 1

                
        return l if  l ** 2 <= x else l - 1
        