class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)<2 and nums[0]==0:
            return 0
        left,right=0,0
        lst=0
        k,ans=0,0
        while right<len(nums):
            if nums[right]==0:
                if k==0:
                    lst=right
                k+=1
            if k==2:
                ans=max(ans,right-left-1)
                left=lst+1
                lst=right
                k-=1
                
            right+=1
            
        return max(ans,right-left-1)     
            
        