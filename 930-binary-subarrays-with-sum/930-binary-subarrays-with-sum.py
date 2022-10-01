class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap={0:1}
        ans,sum_=0,0
        for num in nums:
            sum_+=num
            if sum_-goal in hashmap.keys():
                ans+=hashmap[sum_-goal]    
            hashmap[sum_]=hashmap.get(sum_,0)+1
        return ans    