class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l,r = 1,len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            cnt = 0
            
            cnt = sum(n <= mid for n in nums)
            if cnt > mid:
                dup = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return dup
        
        
        