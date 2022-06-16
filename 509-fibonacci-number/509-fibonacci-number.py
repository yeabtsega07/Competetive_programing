from functools import cache
class Solution:
    def fib(self, n: int) -> int:
        @cache
        def recurse(n):
            if n<2:
                return n
            else:
                return recurse(n-1) + recurse(n-2)
        return recurse(n)
        