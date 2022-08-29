class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=list(str(n))
        if len(nums)<=2 and nums[-1]>nums[0]:
            return int("".join(reversed(nums)))
        pt1=len(nums)-2
        pt2=len(nums)-1
        while pt1>=0:
            if nums[pt1]>=nums[pt2]:
                pt1-=1
                pt2-=1
            else:
                break
        if pt1==-1:
            return -1
        for i in reversed(range(len(nums))):
            if nums[i]>nums[pt1]:
                nums[pt1],nums[i]=nums[i],nums[pt1]
                break
        nums[pt1+1:] = reversed(nums[pt1+1:]) 
        ans=int("".join(nums))
        return ans if ans < 1<<31 else -1
        