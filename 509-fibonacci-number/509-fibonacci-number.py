class Solution:
    def fib(self, n: int) -> int:
        dic={0:0,1:1}
        if n not in dic:
            dic[n]=self.fib(n-1) + self.fib(n-2)
        return dic[n]
        