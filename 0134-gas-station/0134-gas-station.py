class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
       1, 1 -3 + 2 = 0 
       2, 0 - 4 + 3 = -1
       
       1-3 = -2 
       2-4 = -2
       3-5 = -2    -6  0
       4-1 = 3      6
       5-2 = 3
       
       
       2-3 = -1 
       3-4 = -1  -3
       4-3 = -1
      """
        if sum(cost) > sum(gas):
            return -1
        
        
        track, index = 0, 0
        
        for i, num in enumerate(gas):
            
            track += num - cost[i]
            if track < 0:
                track, index = 0, i + 1
                
        return index