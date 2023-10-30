class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        memo = {}
        
        def recur( index, cur ):
            
            if ( index, cur ) in memo:
                return memo[( index, cur )]
            
            if index >= n:
                if cur == target:
                    return 1
                return 0
            res = 0
            for i in range(1, k + 1):
                res += recur(index + 1, cur + i)
            
            memo[( index, cur )] = res
            
            return res
        
        return recur(0, 0) % (10**9 + 7 )
                   
            