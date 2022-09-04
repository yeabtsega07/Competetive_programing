class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        m=10**9+7
        return ((pow(pow(2,p,m)-2,pow(2,p-1)-1,m))*(pow(2,p,m)-1))%m
        