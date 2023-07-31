class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums)<=1:
            return 1
        
        count = 1
        pre = 1
        for i in range(len(nums) - 1):
            
            if nums[i + 1] > nums[i]:
                count = 1 + pre
            elif nums[i + 1] < nums[i]:
                pre = 1 + count
                
        return max(count, pre)    
                                  
                
                
                
                
        