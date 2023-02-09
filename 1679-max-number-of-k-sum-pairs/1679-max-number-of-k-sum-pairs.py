class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, count = len(nums), 0
        left, right = 0, n - 1
        
        while left < right:
            
            if nums[left] + nums[right] == k and right > left:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1 
            else:
                left += 1
                
        return count  
           