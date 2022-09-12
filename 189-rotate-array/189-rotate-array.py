class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        while k>len(nums):
            k=k-len(nums)
        slicer=len(nums)-k
        for i in range(len(nums)):
            if i==slicer:
                break 
            num=nums.pop(0)    
            nums.append(num) 
            
        return nums