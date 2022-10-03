class Solution:
    def heightChecker(self, h: List[int]) -> int:
        if len(h)==1:
            return 0
        count=0
        check=sorted(h)
        for i in range(len(h)):
            if check[i]!=h[i]:
                count+=1
        return count    
        