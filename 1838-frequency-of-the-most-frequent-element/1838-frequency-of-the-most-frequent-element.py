class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        #sliding window
        # condition nums[right]*window length <= sum_ upto nums[right] + k
        
        left,right=0,0
        sum_,res=0,0
        
        while right<len(nums):
            sum_+=nums[right]
            
            while nums[right]*(right-left+1) > sum_+k:
                sum_-=nums[left]
                left+=1
                
            res=max(res,right-left+1)    
            right+=1
            
  
        return res       
                
        