class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)
        track, count = [], 0
        for i in range(n):
            if rocks[i] < capacity[i]:
                diff = capacity[i] - rocks[i]
                track.append(diff)
            else:
                count += 1

        heapify(track)
        i, n = 0, len(track)
        while i < n and additionalRocks:
            diff = heappop(track)
            additionalRocks -= diff
            i += 1
            if additionalRocks >= 0:
                count += 1  
        return count        
        