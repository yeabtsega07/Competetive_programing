class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # for i in range(len(nums)-1):
        #     for j in range(i,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]=nums[j],nums[i]
        nums.sort()
        lft,rgt=0,len(nums)-1
        ans=0
        while lft<rgt:
            ans=max(ans,nums[lft]+nums[rgt])
            lft+=1
            rgt-=1
        return ans    
            
        