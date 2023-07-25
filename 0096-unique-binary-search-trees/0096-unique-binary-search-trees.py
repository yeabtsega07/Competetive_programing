class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = {0:1, 1:1}
        
        def recur ( node ):
            
            if node in dp:
                return dp[node]
            
            curSum = 0
            for root in range(1 , node + 1):
                
                if root  - 1 not in dp:
                    left = recur(root - 1)
                else:
                    left = dp[root - 1]
                
                if (node - root) not in dp:
                    right = recur( node - root )
                else:
                    right = dp[node - root]
                    
                curSum += (left * right)
            
            dp[node] = curSum
            
            return dp[node]
        
        return recur(n)