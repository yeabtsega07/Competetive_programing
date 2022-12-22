class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = [-1, float('inf')]
        
        for i, point in enumerate(points):
            if x == point[0] or y == point[1]:
                cur = abs(point[0] - x) + abs(point[1] - y)
                if ans[1] > cur:
                    ans = [i, cur]
        
        return ans[0]
                
            