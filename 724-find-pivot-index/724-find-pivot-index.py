class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_,lftsum=sum(nums),0
        for i,num in enumerate(nums):
            sum_-=num
            if lftsum==sum_:
                return i
            else:
                lftsum+=num
        return -1    
        