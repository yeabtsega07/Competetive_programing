class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (right + left) // 2
            target = mid *(mid + 1) // 2
            
            if target == n:
                return mid
            elif target > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
                
        