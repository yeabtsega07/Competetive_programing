class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        track, result, curSum = defaultdict(int), 0, 0
        track[0] += 1
        
        for i, num in enumerate(nums):
            
            curSum += num
            result += track[curSum % k]
            track[curSum % k] += 1
        
        return result
        