class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        top,mid,rear=0,0,len(nums)-1
        while mid<=rear:
            if nums[mid]==0:
                nums[mid],nums[top]=nums[top],nums[mid]
                top+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[rear]=nums[rear],nums[mid]
                rear-=1  
                
            
                
                