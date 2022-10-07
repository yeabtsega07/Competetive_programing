class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        pre=sum(chalk)
        k%=pre
        for i , n in enumerate(chalk):
            k-=n
            if k<0:
                return i
        return 0
                
            