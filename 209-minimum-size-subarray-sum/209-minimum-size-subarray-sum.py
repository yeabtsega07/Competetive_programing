class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre=0
        lst=0
        ans=float("inf")
        for i,n in enumerate(nums):
            if not pre:
                pre+=n
                if pre>=target:
                    return 1
                continue
            pre+=n
            while pre>=target:
                ans=min(i-lst+1,ans)
                pre-=nums[lst]
                lst+=1
        return 0 if ans==float("inf") else ans        
                
