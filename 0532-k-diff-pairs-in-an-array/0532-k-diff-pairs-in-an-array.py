class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        track_sum = defaultdict(int)
        possible_nums = set()
        
        for num in nums:
            
            if num in track_sum:
                possible_nums.add((num, track_sum[num]))
            
            track_sum[num + k] = num
        
        return len(possible_nums)