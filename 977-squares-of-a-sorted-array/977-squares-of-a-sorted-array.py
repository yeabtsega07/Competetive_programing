class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        lft,rgt=0,len(nums)-1
        if nums[lft]>=0:
            for i,num in enumerate(nums):
                nums[i]=num*num
            return nums            
        while lft<rgt:
            if nums[lft]**2 >nums[rgt]**2:
                res.append(nums[lft]**2)
                lft+=1
            else:
                res.append(nums[rgt]**2)
                rgt-=1
        res.append(nums[lft]**2)        
        return reversed(res)        
                
        
        