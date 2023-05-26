class Solution:
    def fib(self, n: int) -> int:
        
        track = {0:0,1:1}
        def recur(n):
            if n not in track:
                track[n] = recur(n - 1) + recur(n - 2)
            return track[n]
        
        return recur(n)
        
        