class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count: heapq.heappush(heap, (count, char))
        
        res = []
        while heap:
            count, char = heappop(heap)
            
            if len(res) >= 2 and res[-1] == res[-2] == char:
                
                if not heap: return "".join(res)
                
                count, char = heapreplace(heap, (count, char))
            res.append(char)
            
            if count + 1: heappush(heap, (count + 1, char))
        
        return "".join(res)
        