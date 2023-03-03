class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(nums, k):
            count = 0
            for num in nums:

                count += ceil(num / k)
            
            return count
        
        left, right = 1, max(piles)

        while left <= right:
            
            mid = left + (right - left) // 2
            
            if check(piles, mid) <= h:

                right = mid - 1
            
            else:
                left = mid + 1


        return right if right and check(piles, right) <= h else right + 1
            

            
        