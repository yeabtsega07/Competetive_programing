class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        track, count = [], 0
        for i in range(n):
            diff = capacity[i] - rocks[i]
            heappush(track, diff)
  
        for i in range(n):
            additionalRocks -= heappop(track)
            if additionalRocks >= 0:
                count += 1  
        return count        
