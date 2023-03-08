class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1 and k == 1:
            return 0
        
        half = (2 ** (n - 1)) // 2
        
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - half)