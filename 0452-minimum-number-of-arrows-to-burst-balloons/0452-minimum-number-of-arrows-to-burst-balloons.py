class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        track, ans = 0, 0
        for i in range(len(points)):
            point = points[i]
            
            if ans == 0 or point[0] > track:
                ans, track = ans + 1, point[1]
                
        return ans
                