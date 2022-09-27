class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre=0
        lst=0
        ans=[]
        for i,n in enumerate(nums):
            if not pre:
                pre+=n
                if pre>=target:
                    return 1
                continue
            pre+=n
            while pre>=target:
                ans.append(i-lst+1)
                pre-=nums[lst]
                lst+=1
        return min(ans) if ans else 0        
                
