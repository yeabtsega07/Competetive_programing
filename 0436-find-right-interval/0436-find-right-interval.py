class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = { intervals[i][0]:i  for i in range(len(intervals))}
        listOfStarts = sorted(starts.keys())
        
        def custom_bisect_left ( end ):
            
            left = -1
            right = len(listOfStarts)
            
            while right > left + 1 :
                
                mid = left + (right - left) // 2
                
                if listOfStarts[ mid ] < end:
                    left = mid
                    
                else:
                    right = mid
            
            return right if right < len(listOfStarts) else -1
        
        
        result = []
        for start, end in intervals:
            
            check  = custom_bisect_left( end )
            if check == -1:
                result.append(-1)
            else:    
                result.append(starts[listOfStarts[check]])

                
        
        return result
        
        