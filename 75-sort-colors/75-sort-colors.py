class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lft,dummy,rgt=0,0,len(nums)-1
        while dummy<=rgt:
            if nums[dummy]==0:
                nums[lft],nums[dummy]=nums[dummy],nums[lft]
                lft+=1
                dummy+=1
            elif nums[dummy]==1:
                dummy+=1
            else:
                nums[rgt],nums[dummy]=nums[dummy],nums[rgt]
                rgt-=1
        return nums       
        