class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        prev, result = intervals[0], 0
        
        for cur in intervals:
            
            if  prev[1] > cur[0]:

                if prev[1] >= cur[1]:
                    prev = cur
                
                result += 1

            else:
                prev = cur
        
        return result - 1
        
        
        