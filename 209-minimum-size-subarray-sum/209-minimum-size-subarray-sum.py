class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre=0
        lst=0
        min_=float("inf")
        for i , n in enumerate(nums):
            if not pre and n>=target:
                return 1
            pre+=n
            while pre>=target:
                min_=min(min_,i-lst+1)
                pre-=nums[lst]
                lst+=1
        return min_ if min_!=float("inf") else 0        
                
                