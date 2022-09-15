class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lst=-1
        snd=-1
        max_=0
        curmax=0
        lstf=0
        for i, fru in enumerate(fruits):
            if fru==lst or fru==snd:
                curmax+=1
            else:
                curmax=lstf+1
            if fru==lst:
                lstf+=1
            else:
                lstf=1
                snd=lst
                lst=fru
            max_=max(max_,curmax)
        return max_    

        