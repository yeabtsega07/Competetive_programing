class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        count=0
        for num in nums:
            if num!=mid:
                count+=abs(num-mid)
        return count        
        