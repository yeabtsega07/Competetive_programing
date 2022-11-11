class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left, res = -1, 0
        
        for right in range(len(seats)):
            
            if seats[right] == 1:
                if left != -1:
                    res = max(res, (right - left) // 2)
                else:
                    res = max(res , right)
                    # print(right)
                
                left = right
        
        if seats[right] != 1:
            res = max(res, right -left )
        
        return res
            
        