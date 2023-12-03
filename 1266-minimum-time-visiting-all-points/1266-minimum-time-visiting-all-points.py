class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        
        start = points[0]
        res = 0
        
        for i in range(1, len(points)):
            
            res += max(abs(points[i][0] - start[0]), abs(points[i][1] - start[1]))
            start = points[i]
        
        return res