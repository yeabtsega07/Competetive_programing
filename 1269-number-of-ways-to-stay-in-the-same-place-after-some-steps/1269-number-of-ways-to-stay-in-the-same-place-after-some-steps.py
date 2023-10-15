class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        memo = {}
        
        def recur(index, count):
            
            if (index, count) in memo:
                return memo[(index, count)]
            
            if  not (0 <= index <  arrLen):
                return 0
            
            if count == steps:
                if index == 0:
                    return 1
                return 0
            
            res = recur(index + 1, count + 1) + recur(index - 1, count + 1) + recur(index, count + 1)
            memo[(index, count)] = res
            
            return res
        
        return recur(0, 0) % (10 ** 9 + 7)
    
        