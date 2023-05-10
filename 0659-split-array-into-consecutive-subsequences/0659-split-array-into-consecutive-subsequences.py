class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        track = defaultdict(list)
        
        for num in nums:
            
            if track[num - 1]:
                last = heappop(track[num - 1])
                heappush(track[num], last + 1)
            else:
                heappush(track[num], 1)
        

        for cur in track.values():
            if cur and cur[0] < 3:
                return False
        
        return True
        