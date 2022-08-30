class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hind=0
        n=len(citations)
        if n==0:
            return 0
        citations.sort()
        if citations[0]>=n:
            return n
        for i in range(n):
            if i>=citations[n-1-i]:
                hind=i
                break
        return hind        
            