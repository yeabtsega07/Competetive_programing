class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k==1 and n==1:
            return 0
        half=pow(2,n-1)//2
        if k<=half:
            return int(self.kthGrammar(n-1,k))
        else:
            return int(not self.kthGrammar(n-1,k-half))
        