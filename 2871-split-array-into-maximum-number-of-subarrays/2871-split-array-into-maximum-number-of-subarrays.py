class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        min_and = nums[0]
        
        for i in range(1, len(nums)):
            min_and &= nums[i]
        
        if not min_and:
            
            left, count, cur = 0, 0, nums[0]
            for right in range(1, len(nums)):
                
                if not cur:
                    cur = nums[right]
                    left = right
                    count += 1
                
                cur &= nums[right]
            
            if not cur:
                count += 1
            return count
        
        return 1
                    
                