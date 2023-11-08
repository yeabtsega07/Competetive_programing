class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # simulation
        
        heap = []
        for  i in range(len(dist)):
            time = dist[i] / speed[i]
            heappush(heap, time)
        
        count_time = 0
        
        while heap:
            
            min_val = heappop(heap)
            
            if count_time < min_val:
                count_time += 1
            else:
                break
        
        return count_time
            
            
            