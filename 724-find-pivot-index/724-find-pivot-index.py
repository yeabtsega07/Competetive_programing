class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_=sum(nums)
        leftsum=0
        for i , num in enumerate (nums):
            sum_-=num
            if leftsum==sum_:
                return i
            else:
                leftsum+=num
            
        return -1    


  
        