class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        if n == 2:
            return 1 if roads else 0
        
        track = defaultdict(list)
        
        for road in roads:
            
            track[road[0]].append(road[1])
            track[road[1]].append(road[0])

        result = 0
        
        for i in range ( n - 1 ):
            
            for j in range (i + 1,  n):
                
                current = track[i] + track[j]
                if i in current and j in current:
                    current.pop()
                
                result = max(len(current), result)
        
        return result
        