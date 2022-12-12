class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {1:1,2:2}
        def helper (n):
            if n not in dict.keys():
                dict[n] = helper(n-1) + helper(n-2)
            return dict[n]
        return helper(n)
  
        
        