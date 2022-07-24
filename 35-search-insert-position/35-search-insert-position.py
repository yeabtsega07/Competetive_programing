class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            targ=nums[mid]
            if targ==target:
                return mid
            if targ>target:
                high=mid-1
            else:
                low=mid+1
        return low     
                