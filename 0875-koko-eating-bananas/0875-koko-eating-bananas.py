class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(nums, k):
            count = 0
            for num in nums:
                
                count += ceil(num / k)
            
            return count
        
        left, right = 1, max(piles)
        ans = 0
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if check(piles, mid) <= h:
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1

        
        return ans
            

            
        