class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)  
        players = [[ages[i], scores[i]] for i in range(n)]
        players.sort()
        
        dp = {}
        def recur(index, pre):
            
            if (index, pre) in dp:
                return dp[(index, pre)]
            
            if index >= n:
                return 0
            
            take = 0
            if pre <= players[index][1]:

                take = max(take, recur(index + 1, players[index][1]))
                take += players[index][1]   
                
            notTake = recur(index + 1, pre) 
            dp[(index, pre)] = max(take, notTake)
            
            return max(take, notTake)
        
        return recur(0, -float("inf"))
    
            
            