class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls, ans = [], [0] * len(boxes)
        
        for i, num in enumerate(list(boxes)):
            if int(num) > 0:
                balls.append(i)
        
        for i, num in enumerate(list(boxes)):
            cur = 0
            for ball in balls:
                cur += abs(i - ball)
            ans[i] = cur
        
        return ans