class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        result = 0
        
        for num in nums:
            
            if num - 1 not in set_nums:
                cur_count = 1
                
                while num + 1 in set_nums:
                    cur_count += 1
                    num += 1
                    
                result = max(cur_count, result)
        
        return result
            
        
        
        