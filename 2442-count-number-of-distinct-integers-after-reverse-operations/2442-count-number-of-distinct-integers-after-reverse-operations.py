class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        track = set(nums)
        for num in nums:
            cur = 0
            while num:
                temp = num % 10
                cur = cur * 10 + temp
                num = num // 10
            
            track.add(cur)
    
        return len(track)    
        