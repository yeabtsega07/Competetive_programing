class Solution:
    def chalkReplacer(self, chalk: List[int], p: int) -> int:

        pre=sum(chalk)
        k=p%pre
        for i , n in enumerate(chalk):
            k-=n
            if k<0:
                return i
        return 0
                
            