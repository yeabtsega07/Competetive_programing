class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        dp = {}
        events.sort()

        def recur (index, k):
            if k == 0:
                return 0
            
            if index >= len(events):
                return 0
            
            if (index, k) in dp:
                return dp[(index, k)]
            

            cur = index
            while cur < len(events) and events[cur][0] <= events[index][1]:
                cur += 1
                
            take = events[index][2] + recur(cur, k - 1)


            notTake = recur(index + 1,k)

            dp[(index, k)] = max(take ,notTake)

            return dp[(index ,k)]
    
        return recur(0,k)