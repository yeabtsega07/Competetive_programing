class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        track = { intervals[i][0]:i for i in range(len(intervals))}
        starts = sorted(track.keys())

        result = []
        
        for start, end  in intervals:
            
            temp = bisect_left(starts, end )
            if temp >= len(starts):
                result.append(-1)
            else:
                result.append(track[starts[temp]])
        
        return result
                
                