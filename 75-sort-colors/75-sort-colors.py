class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        track=[0]*3
        for num in nums:
            if num==0:
                track[0]+=1
            elif num==1:
                track[1]+=1
            else:
                track[2]+=1
        l=0        
        for i, num in enumerate(track):
            while num>0:
                nums[l]=i
                l+=1
                num-=1    
        return nums        
            
                
                