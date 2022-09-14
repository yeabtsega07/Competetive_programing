class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow=0
        max_=0
        for fast in range(len(nums)):
            if nums[fast]==0:
                k-=1
            
            while k<0:
                if nums[slow]==0:
                    k+=1
                slow+=1
            
            max_=max(max_,fast-slow+1)
        return max_   
        