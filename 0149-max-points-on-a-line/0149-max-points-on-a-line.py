class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        if length == 1:
            return 1

        def helper(x1, y1, x2, y2): # calculate the line equation
            if x1 == x2:
                return (1, 0, -x1)
            slope = (y1 - y2) / (x1 - x2)
            constant = y1 - slope * x1
            return (slope, -1, constant)

        ans = 0
        for i in range(length):
            track = collections.defaultdict(set)
            x1, y1 = points[i]
            for j in range(i + 1, length):
                x2, y2 = points[j]
                line = helper(x1, y1, x2, y2)
                track[line].add((x1, y1))
                track[line].add((x2, y2))
                ans = max(ans, len(track[line]))
        return ans
        