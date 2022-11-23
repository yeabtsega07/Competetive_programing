class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            
            if diff > 0:
                heappush(jumps, diff)
            
                if len(jumps) > ladders:
                    jump = heappop(jumps)
                    bricks -= jump
                
                if bricks < 0:
                    return i
        
        return len(heights) - 1
                
