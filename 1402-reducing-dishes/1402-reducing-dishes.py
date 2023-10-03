class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        
        result, curSum = 0, 0
        while satisfaction and curSum + satisfaction[-1] > 0:
            curSum += satisfaction.pop()
            result += curSum
        
        return result
        