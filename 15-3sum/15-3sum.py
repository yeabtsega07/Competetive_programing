class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i , num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
                
            lft,rgt=i+1,len(nums)-1
            while lft<rgt:
                if num+nums[lft]+nums[rgt]<0:
                    lft+=1 
                elif num+nums[lft]+nums[rgt]>0:
                    rgt-=1
                else:
                    ans.append([num,nums[lft],nums[rgt]])
                    lft+=1
                    while nums[lft]==nums[lft-1] and lft<rgt:
                        lft+=1
        return ans                
 
 
            

            
        