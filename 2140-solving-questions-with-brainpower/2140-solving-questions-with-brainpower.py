class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        dp = {}
        
        def recur ( index ):
            
            if index >= len(questions):
                return 0
            
            if index in dp:
                return dp[index]
            
            solve = questions[index][0] + recur( index + questions[index][1] + 1 )
            notSolve = recur(index + 1)
            
            dp[index] = max(solve, notSolve)
            
            return dp[index]
            
        return recur( 0 )