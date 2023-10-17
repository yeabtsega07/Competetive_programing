class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        memo = {}
        
        def recur ( index, is_even ):
            
            if (index, is_even) in memo:
                return memo[(index, is_even)]
            
            if index >= len(nums):
                return 0
           
            if is_even: 
                cur = nums[index]
            else:
                cur = -nums[index]
            
            take = recur(index + 1, 1 - is_even) +  cur
            notTake = recur(index + 1, is_even)
            
            memo[(index, is_even)] = max(take, notTake)
            
            return memo[(index, is_even)]
        
        return recur(0, 1)
            
            