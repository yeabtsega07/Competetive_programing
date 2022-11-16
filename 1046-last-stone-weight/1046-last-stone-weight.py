class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i  for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if second > first:
                heapq.heappush(stones, first - second)
                
        stones.append(0)
        return - stones[0]