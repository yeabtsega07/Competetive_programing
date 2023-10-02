class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        target = ceil(sum(stones) / 2)
        
        dp = {}
        def recur ( index, track ):
            
            if track >= target or index >= len(stones):
                return abs(track - (sum(stones) - track))
            
            if (index, track) in dp:
                return dp[(index, track)]
            
            dp[(index, track)] = min(recur(index + 1, track), recur(index + 1, track + stones[index]))
            
            return dp[(index, track)]
        
        return recur(0, 0)
        